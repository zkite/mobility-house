from __future__ import annotations

import asyncio
from typing import Callable

import aio_pika
from aiormq.exceptions import AMQPConnectionError, ConnectionChannelError
from loguru import logger

from app.broker.exceptions import (
    BrokerConnectionError,
    ChannelBrokerError,
    QueueBrokerError,
    RoutingKeyBrokerError,
    UrlBrokerError,
)


class Broker:
    def __init__(self, url: str, routing_key: str) -> None:
        self._url = url
        self._routing_key = routing_key
        self._connection = None
        self._channel = None
        self._message_queue = None
        self._queue = None

    @property
    def url(self):
        """RabbitMQ  connections url"""
        if self._url:
            return self._url
        raise UrlBrokerError("Connection url is empty")

    @property
    def channel(self):
        """RabbitMQ  channel"""
        if self._channel:
            return self._channel
        raise ChannelBrokerError("Channel is undefined")

    @property
    def routing_key(self):
        """The routing key of the message"""
        if self._routing_key:
            return self._routing_key
        raise RoutingKeyBrokerError("Routing key is empty")

    @property
    def queue(self):
        """Message queue"""
        if self._queue:
            return self._queue
        raise QueueBrokerError("Queue is undefined")

    async def publish(self, message: str) -> None:
        """Publish message to a queue"""
        logger.info(f"publish message: {message}")
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=self.routing_key,
        )

    async def consume(self, process_message: Callable) -> None:
        """Consume message from a queue"""
        async with self.queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    logger.info(f"consume message: {message.body}")
                    process_message(message.body)
                    await asyncio.sleep(1)

    async def __aenter__(self) -> Broker:
        """Make a broker context"""
        logger.debug("instantiate broker; initiate connection to rabbitmq")
        try:
            self._connection = await aio_pika.connect(self.url)
        except AMQPConnectionError:
            raise BrokerConnectionError("Broker connection error")
        try:
            self._channel = await self._connection.channel()
        except ConnectionChannelError:
            raise ChannelBrokerError("Can't connect to the channel")
        self._queue = await self.channel.declare_queue(
            self.routing_key, auto_delete=True
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit broker context and close a connection"""
        logger.debug("exit from broker context; close rabbitmq connection")
        await self._connection.close()
