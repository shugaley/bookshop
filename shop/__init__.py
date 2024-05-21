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
        self.cart: list[Book] = []

    def process(self, cmd: str) -> str:
        '''Process command'''
        msg = f"Неизвестная команда: '{cmd}'\n"

        if cmd.startswith("Добавить книгу"):
            self.__add_book(cmd.split("Добавить книгу")[1])
            new_book = self.catalog[-1]
            msg = "Книга "
            msg += self.__transform_book_to_str(new_book)
            msg += " добавлена\n"

        elif cmd.startswith("Удалить книгу"):
            old_book = self.__remove_book(cmd.split("Удалить книгу")[1])
            msg = "Книга "
            msg += self.__transform_book_to_str(old_book)
            msg += " удалена\n"

        elif cmd.startswith("Показать каталог"):
            msg = "Каталог:\n"
            msg += self.__show_catalog()

        elif cmd.startswith("Добавить в корзину"):
            new_book_cart = self.__add_book_to_cart(
                cmd.split("Добавить в корзину ")[1])
            msg = "Книга "
            msg += self.__transform_book_to_str(new_book_cart)
            msg += " добавлена в корзину"

        elif cmd.startswith("Удалить из корзины"):
            old_book_cart = self.__remove_book_from_cart(
                cmd.split("Удалить из корзины ")[1])
            msg = "Книга "
            msg += self.__transform_book_to_str(old_book_cart)
            msg += " удалена из корзины"

        return msg

    def __transform_book_to_str(self, book: Book) -> str:
        '''Transform Book to str'''
        ret = f"{book.title} {book.author} {book.year} "
        ret += f"{book.price} {book.publisher} {book.genre}"
        return ret

    def __find_book_by_title(self, book_title: str, lst: list[Book]) -> Book:
        '''Find book in catalog or cart by title'''
        book = Book("", "", "", "", "", "")
        for i_book in lst:
            if i_book.title == book_title:
                book = i_book
                break
        return book

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

    def __show_catalog(self) -> str:
        '''Return full current catalog'''
        ret = ""
        for i_book in self.catalog:
            ret += self.__transform_book_to_str(i_book)
            ret += "\n"
        return ret

    def __add_book_to_cart(self, book_title: str) -> Book:
        '''Add book to cart'''
        book = self.__find_book_by_title(book_title, self.catalog)
        self.cart.append(book)
        return book

    def __remove_book_from_cart(self, book_title: str) -> Book:
        '''Remove book from cart'''
        book = self.__find_book_by_title(book_title, self.cart)
        self.cart.remove(book)
        return book
