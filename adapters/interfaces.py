from abc import ABC, abstractmethod
from typing import List

from domain.book.dto import *
from domain.book.model import Book
from domain.user.dto import *
from domain.user.model import User


class UserServiceI(ABC):
    @abstractmethod
    def get_users(self, limit: int, offset: int) -> List[User]: pass

    @abstractmethod
    def get_user(self, user_id) -> User: pass

    @abstractmethod
    def create_user(self, user: CreateUserDTO) -> User: pass

    @abstractmethod
    def delete_user(self, user_id): pass

    @abstractmethod
    def update_user(self, user: UpdateUserDTO): pass

    @abstractmethod
    def partially_update(self, user: PartiallyUpdateUserDTO): pass


class BookServiceI(ABC):
    @abstractmethod
    def get_books(self, limit: int, offset: int) -> List[Book]: pass

    @abstractmethod
    def get_book(self, book_id) -> Book: pass

    @abstractmethod
    def create_book(self, book: CreateBookDTO) -> Book: pass

    @abstractmethod
    def delete_book(self, book_id): pass

    @abstractmethod
    def update_book(self, book: UpdateBookDTO): pass

    @abstractmethod
    def partially_update(self, book: PartiallyUpdateBookDTO): pass

    @abstractmethod
    def return_book(self, book_id: int): pass

    @abstractmethod
    def take_book(self, book_id: int, owner: str): pass
