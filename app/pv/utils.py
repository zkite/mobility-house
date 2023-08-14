import arrow
from numpy import exp


def gauss(x: float, A: float, x_mean: float, sigma: float) -> float:
    """Gaussian function"""
    return A * exp(-((x - x_mean) ** 2) / (2 * sigma**2))


def to_file(file_path: str, data: dict) -> None:
    """Write data to a file"""
    with open(file_path, "a") as f:
        row = f"{data['datetime']}; Meter(kW): {data['meter']}; PV(kW): {data['pv']}; Total(kW): {data['total']};\n"
        f.write(row)


def to_seconds(dt: str) -> int:
    """Convert time to seconds"""
    time = arrow.get(dt).time()
    return time.hour * 3600 + time.minute * 60 + time.second


def to_kw(value: float):
    """Convert Watts Into Kilowatt"""
    return round(value / 1000, 3)
