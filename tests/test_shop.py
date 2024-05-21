import pytest
from shop import Shop

@pytest.fixture
def shop():
    return Shop()

default_book = "Название Автор 2000 1000 Издательство Жанр"

def test_unknown_command(shop):
    res = shop.process("Неизвестная комманда")
    assert(res == "Неизвестная команда: 'Неизвестная комманда'\n")

def test_add_to_catalog(shop):
    res = shop.process(f"Добавить книгу {default_book}")
    assert(res == f"Книга {default_book} добавлена\n")

def test_remove_from_catalog(shop):
    shop.process(f"Добавить книгу {default_book}")
    res = shop.process(f"Удалить книгу {default_book}")
    assert(res == f"Книга {default_book} удалена\n")
    res = shop.process(f"Удалить книгу {default_book}")
    assert(res == f"Книга       удалена\n")

def test_show_catalog(shop):
    shop.process("Добавить книгу Название1 Автор1 2000 1000 Издательство Жанр")
    shop.process("Добавить книгу Название2 Автор2 2000 1000 Издательство Жанр")
    shop.process("Удалить книгу Название2 Автор2 2000 1000 Издательство Жанр")
    shop.process("Добавить книгу Название3 Автор3 2000 1000 Издательство Жанр")
    res = shop.process("Показать каталог")
    assert(res == "Каталог:\n"
                  "Название1 Автор1 2000 1000 Издательство Жанр\n"
                  "Название3 Автор3 2000 1000 Издательство Жанр\n")

def test_add_to_cart(shop):
    shop.process(f"Добавить книгу {default_book}")
    res = shop.process("Добавить в корзину Название")
    assert(res == f"Книга {default_book} добавлена в корзину")

def test_remove_from_cart(shop):
    shop.process("Добавить книгу Название1 Автор1 2000 1000 Издательство Жанр")
    shop.process(f"Добавить книгу {default_book}")
    shop.process("Добавить в корзину Название1")
    shop.process("Добавить в корзину Название")
    res = shop.process(f"Удалить из корзины Название")
    assert(res == f"Книга {default_book} удалена из корзины")
    res = shop.process(f"Удалить из корзины Название2")
    assert(res == f"Книга       удалена из корзины")