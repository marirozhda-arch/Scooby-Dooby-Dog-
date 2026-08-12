from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Pet:
    icon: str
    name: str
    breed: int 
    diseases: str
    health_status: int
    story: str
    age: date
    color: list
    character: list 
    id: int | None = None
