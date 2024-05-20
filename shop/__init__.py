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


class Shop:
    '''Shop worker'''
    def __init__(self) -> None:
        self.catalog: list[Book] = []

    def process(self, cmd: str) -> str:
        '''Process command and return command's status report message'''
        msg = f"Неизвестная команда: '{cmd}'\n"

        if cmd.startswith("Добавить книгу"):
            self.add_book(cmd.split("Добавить книгу")[1])
            new_book = self.catalog[-1]
            msg = "Книга "
            msg += f"{new_book.title} {new_book.author} {new_book.year} "
            msg += f"{new_book.price} {new_book.publisher} {new_book.genre} "
            msg += "добавлена\n"

        return msg

    def add_book(self, book_info: str) -> bool:
        '''Add book to catalog'''
        book = book_info.strip().split(' ')
        self.catalog.append(
            Book(book[0], book[1], book[2], book[3], book[4], book[5]))
        return True
