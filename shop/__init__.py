'''Module shop implement e-bookshop'''
from dataclasses import dataclass


@dataclass
class Book:
    '''Book description'''
    title: str
    author: str
    year: str
    price: str
    publisher: str
    genre: str


# pylint: disable=too-few-public-methods
class Shop:
    '''Shop worker'''
    def __init__(self) -> None:
        self.catalog: list[Book] = []

    def process(self, cmd: str) -> str:
        '''Process command and return command's status report message'''
        msg = f"Неизвестная команда: '{cmd}'\n"

        if cmd.startswith("Добавить книгу"):
            self.__add_book(cmd.split("Добавить книгу")[1])
            new_book = self.catalog[-1]
            msg = "Книга "
            msg += self.__transform_book_to_msg(new_book)
            msg += "добавлена\n"

        elif cmd.startswith("Удалить книгу"):
            old_book = self.__remove_book(cmd.split("Удалить книгу")[1])
            msg = "Книга "
            msg += self.__transform_book_to_msg(old_book)
            msg += "удалена\n"

        return msg

    def __transform_book_to_msg(self, book: Book) -> str:
        '''Transform Book to str'''
        msg = f"{book.title} {book.author} {book.year} "
        msg += f"{book.price} {book.publisher} {book.genre} "
        return msg

    def __add_book(self, book_info: str) -> bool:
        '''Add book to catalog'''
        book = book_info.strip().split(' ')
        self.catalog.append(
            Book(book[0], book[1], book[2], book[3], book[4], book[5]))
        return True

    def __remove_book(self, book_info: str) -> Book:
        '''Remove book from catalog and return removed book'''
        book = book_info.strip().split(' ')
        book_entity = \
            Book(book[0], book[1], book[2], book[3], book[4], book[5])
        self.catalog.remove(book_entity)
        return book_entity
