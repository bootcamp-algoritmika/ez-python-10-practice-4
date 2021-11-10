from abc import ABC, abstractmethod

from domain.book.model import Book


class BookStorageI(ABC):

    @abstractmethod
    def get_one(self, book_id: int):
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int):
        pass

    @abstractmethod
    def create(self, book: Book):
        pass

    @abstractmethod
    def update(self, book: Book):
        pass

    @abstractmethod
    def delete(self, book_id: int):
        pass
