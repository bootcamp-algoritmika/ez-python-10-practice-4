from dataclasses import dataclass


@dataclass
class CreateBookDTO:
    name: str
    author: str
    year: int
    owner: str = None


@dataclass
class UpdateBookDTO:
    id: int
    name: str
    owner: str
    author: str
    year: int


@dataclass
class PartiallyUpdateBookDTO:
    id: int
    owner: str = None
    name: str = None
    author: str = None
    year: int = None
