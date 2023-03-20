import asyncio

from app.broker import Broker
from app.constants import AMQP_URL, QUEUE_NAME
from app.pv.core import Pv


async def main():
    """PV entry point"""
    meter = Pv(3250, 2, Broker(AMQP_URL, QUEUE_NAME))
    await meter.consume()


if __name__ == "__main__":
    asyncio.run(main())
