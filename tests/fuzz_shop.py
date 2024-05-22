import atheris
import sys
import random
with atheris.instrument_imports():
    from shop import Shop

commands = [
    "Добавить книгу", "Удалить книгу", "Показать каталог",
    "Добавить в корзину", "Удалить из корзины",
    "Оформить заказ", "Отменить заказ", "Доставить заказ", "Вернуть заказ",
    "Статус заказа", "Неизвестная комманда"
    ]

errors = []

def generate_input(input_bytes):
    cmd = random.choice(commands)

    try:
        fdp = atheris.FuzzedDataProvider(input_bytes)
        data = fdp.ConsumeUnicode(sys.maxsize)
    except UnicodeEncodeError:
        data = ""

    args = []
    n_args = random.randint(0, 10)
    for _ in range(n_args):
        chars = random.choices(data, k=random.randint(0, len(data)))
        arg = ''.join(chars)
        if len(arg) != 0:
            args.append(arg)

    return cmd + ' '.join(args)

@atheris.instrument_func
def test_fuzz(input_bytes):
    shop = Shop()
    n_process = random.randint(1, 10)
    for _ in range(n_process):
            data = generate_input(input_bytes)
            try:
                shop.process(data)
            except Exception as e:
                errors.append(e)

atheris.Setup(sys.argv, test_fuzz)
atheris.Fuzz()
print(len(errors))