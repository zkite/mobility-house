import asyncio
import json
import random

import arrow

from app.broker import Broker
from app.constants import DATETIME_FORMAT


class Meter:
    def __init__(
        self, min_pwr: float, max_pwr: float, delay: int, broker: Broker
    ) -> None:
        self.min_pwr = min_pwr
        self.max_pwr = max_pwr
        self.delay = delay
        self.broker = broker

    async def send_messages(self) -> None:
        """Send message to a queue"""
        async with self.broker as b:
            while True:
                await b.publish(
                    json.dumps(
                        {
                            "timestamp": arrow.utcnow().format(DATETIME_FORMAT),
                            "value": random.uniform(self.min_pwr, self.max_pwr),
                        }
                    )
                )
                await asyncio.sleep(self.delay)
