class BookNotFoundException(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(BookNotFoundException, self).__init__(*args, **kwargs)


class BookIsBusyException(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(BookIsBusyException, self).__init__(*args, **kwargs)