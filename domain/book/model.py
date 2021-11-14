from datetime import datetime

from domain.book.exceptions import BookIsBusyException


class Book:
    def __init__(self, name: str, author: str, year: int,
                 created_date: str = datetime.strftime(datetime.utcnow(), "%s"), modified_date: str = None, id: int = None, owner: str = None):
        self.id: int = id
        self.owner: str = owner
        self.name: str = name
        self.author: str = author
        self.year: int = year
        self.created_date: str = created_date
        self.modified_date: str = modified_date

    def change_owner(self, nowner: str):
        if self.owner is not None:
            raise BookIsBusyException(f"book has an owner: {self.owner}")
        self.owner = nowner