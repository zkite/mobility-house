import pytest
from app.broker import Broker
from app.broker import exceptions


def test_broker_get_url_error():
    with pytest.raises(exceptions.UrlBrokerError):
        Broker(url=None, routing_key="fake_routing_key").url


def test_broker_get_url_ok():
    url = "fake_url"
    assert Broker(url=url, routing_key="fake_routing_key").url == url


@pytest.mark.asyncio
async def test_broker_connection_error():
    with pytest.raises(exceptions.BrokerConnectionError):
        async with Broker(
            url="amqp://localhost:4321", routing_key="fake_routing_key"
        ) as b:
            ...


def test_broker_get_channel_error():
    with pytest.raises(exceptions.ChannelBrokerError):
        Broker(url="fake_url", routing_key="fake_routing_key").channel


def test_broker_get_queue_error():
    with pytest.raises(exceptions.QueueBrokerError):
        Broker(url="fake_url", routing_key="fake_routing_key").queue
