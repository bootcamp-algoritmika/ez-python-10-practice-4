from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    id: int = None
