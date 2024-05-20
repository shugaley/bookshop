import pytest
from shop import Shop

@pytest.fixture
def shop():
    return Shop()

def test_unknown_command(shop):
    res = shop.process("Неизвестная комманда")
    assert(res == "Неизвестная команда: 'Неизвестная комманда'\n")

def test_add_catalog(shop):
    res = shop.process("Добавить книгу "
                       "Название Автор 2000 1250 Издательство Жанр")
    assert(res == "Книга Название Автор 2000 1250 Издательство Жанр "
                  "добавлена\n")

def test_remove_catalog(shop):
    res = shop.process("Добавить книгу "
                       "Название Автор 2000 1250 Издательство Жанр")
    res = shop.process("Удалить книгу "
                       "Название Автор 2000 1250 Издательство Жанр")
    assert(res == "Книга Название Автор 2000 1250 Издательство Жанр "
                  "удалена\n")