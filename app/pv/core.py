import json
from typing import List

import numpy as np
from loguru import logger

from app.broker import Broker
from app.constants import FILE_PATH
from app.pv.utils import gauss, to_file, to_kw, to_seconds


class Pv:
    def __init__(self, max_pvr: float, time_delta: int, broker: Broker) -> None:
        self.broker = broker
        self.max_pvr = max_pvr
        self.time_delta = time_delta
        self._data = []

    @property
    def data(self) -> List[float]:
        """Simulated data for each second of a day"""
        if not self._data:
            for x in np.linspace(0, 24, 86400):
                self._data.append(gauss(x, self.max_pvr, 14, 3))
        return self._data

    def get_value(self, v):
        """Get value from simulated data"""
        try:
            return self.data[v]
        except IndexError:
            logger.error("Can't get value from simulated data")

    async def consume(self) -> None:
        """Consume message from queue"""
        async with self.broker as b:
            await b.consume(self.process_message)

    def process_message(self, message: str) -> None:
        """Process consumed message"""
        meter = json.loads(message)
        value = self.get_value(to_seconds(meter["timestamp"]))
        to_file(
            FILE_PATH,
            {
                "datetime": meter["timestamp"],
                "meter": to_kw(meter["value"]),
                "pv": to_kw(value),
                "total": to_kw(meter["value"] + value)
            }
        )
