from datetime import datetime

from domain.book.exceptions import BookNotFoundException
from domain.book.model import Book
from domain.book.storage import BookStorageI

books_data = {
    '1': Book(id=1, name="Book1", author="author1", year=2001, created_date=datetime.strftime(datetime.utcnow(), "%s")),
    '2': Book(id=2, name="Book2", author="author2", year=2002, created_date=datetime.strftime(datetime.utcnow(), "%s")),
    '3': Book(id=3, name="Book3", author="author3", year=2003, created_date=datetime.strftime(datetime.utcnow(), "%s")),
    '4': Book(id=4, name="Book4", author="author4", year=2004, created_date=datetime.strftime(datetime.utcnow(), "%s")),
    '5': Book(id=5, name="Book5", author="author5", year=2005, created_date=datetime.strftime(datetime.utcnow(), "%s")),
}


class BookStorage(BookStorageI):

    def create(self, book: Book):
        new_book_id = len(books_data.keys()) + 1
        books_data[str(new_book_id)] = book
        book.id = new_book_id
        return book

    def update(self, book: Book):
        if str(book.id) not in books_data.keys():
            raise BookNotFoundException(message="book not found")
        books_data.update({str(book.id): book})
        return book

    def delete(self, book_id: int):
        try:
            books_data.pop(str(book_id))
        except KeyError as e:
            raise BookNotFoundException(message="book not found")

    def get_one(self, book_id: str):
        try:
            return books_data[str(book_id)]
        except KeyError as e:
            raise BookNotFoundException(message="book not found")

    def get_all(self, limit: int, offset: int):
        books = list(books_data.values())[offset:limit + offset]
        return books
