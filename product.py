from dataclasses import dataclass
from datetime import date

@dataclass(slots=True)
class Product:
    icon: str
    best_before_date: date
    name: str
    category: str
    price: int
    rating: float
    id: int | None = None
