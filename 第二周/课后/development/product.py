from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


def total(items: list[Product]) -> float:
    return sum(item.price for item in items)