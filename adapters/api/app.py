from wsgiref import simple_server

import falcon
from falcon import App

from adapters.api.controllers import UsersResource, UserResource, BooksResource, BookResource, BookStatus, BookReturn, \
    BookTake
from adapters.db.book.storage import BookStorage
from adapters.db.user.storage import UserStorage
from domain.book.service import BookService
from domain.user.service import UserService

user_storage = UserStorage()
user_service = UserService(storage=user_storage)

book_storage = BookStorage()
book_service = BookService(storage=book_storage)


def create_app() -> App:
    app = falcon.App()

    users_view = UsersResource(service=user_service)
    user_view = UserResource(service=user_service)

    books_view = BooksResource(service=book_service)
    book_view = BookResource(service=book_service)
    book_status = BookStatus(service=book_service)
    book_return = BookReturn(service=book_service)
    book_take = BookTake(service=book_service)

    app.add_route('/users/', users_view)
    app.add_route('/users/{user_id}', user_view)
    app.add_route('/books/', books_view)
    app.add_route('/books/{book_id}', book_view)
    app.add_route('/books/{book_id}/status', book_status)
    app.add_route('/books/{book_id}/take', book_take)
    app.add_route('/books/{book_id}/return', book_return)
    return app


if __name__ == '__main__':
    app = create_app()
    httpd = simple_server.make_server('127.0.0.1', 1234, app)
    httpd.serve_forever()

