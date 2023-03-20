import asyncio

from app.broker import Broker
from app.constants import AMQP_URL, QUEUE_NAME
from app.meter.core import Meter


async def main():
    """Meter entry point"""
    meter = Meter(0, 9000, 2, Broker(AMQP_URL, QUEUE_NAME))
    await meter.send_messages()


if __name__ == "__main__":
    asyncio.run(main())
