from typing import List

from adapters.interfaces import BookServiceI
from domain.book.dto import CreateBookDTO, UpdateBookDTO, PartiallyUpdateBookDTO
from domain.book.model import Book
from domain.book.storage import BookStorageI


class BookService(BookServiceI):
    def __init__(self, storage: BookStorageI):
        self.storage = storage

    def return_book(self, book_id: int):
        book = self.get_book(book_id=book_id)
        book.owner = None
        self.storage.update(book)

    def take_book(self, book_id: int, owner: str):
        book = self.get_book(book_id=book_id)
        book.change_owner(nowner=owner)
        self.storage.update(book)

    def get_books(self, limit: int, offset: int) -> List[Book]:
        # in real life any filters or something else
        books = self.storage.get_all(limit, offset)
        return books

    def get_book(self, book_id) -> Book:
        books = self.storage.get_one(book_id=book_id)
        return books

    def create_book(self, dto: CreateBookDTO) -> Book:
        book = Book(**dto.__dict__)
        return self.storage.create(book=book)

    def delete_book(self, book_id) -> None:
        self.storage.delete(book_id=book_id)

    def update_book(self, dto: UpdateBookDTO):
        old_book = self.get_book(dto.id)
        book = Book(**dto.__dict__)
        if old_book.owner != book.owner:
            book.owner = old_book.owner
            book.change_owner(dto.owner)
        self.storage.update(book=book)

    def partially_update(self, book: PartiallyUpdateBookDTO):
        old_book = self.get_book(book.id)
        if book.owner is not None:
            old_book.change_owner(book.owner)
        if book.name is not None:
            old_book.name = book.name
        if book.author is not None:
            old_book.author = book.author
        if book.year is not None:
            old_book.year = book.year

        self.storage.update(book=old_book)
