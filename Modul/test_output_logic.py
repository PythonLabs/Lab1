# test_output_logic.py

from output_logic import print_prices

def test_print_prices(capsys):
    # Входные данные
    sweets = {
        'печенье': [
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'ашан', 'price': 10.99},
        ],
        'конфеты': [
            {'shop': 'магнит', 'price': 30.99},
            {'shop': 'пятерочка', 'price': 32.99},
        ],
    }

    # Ожидаемый вывод
    expected_output = (
        "печенье:\n"
        "  пятерочка: 9.99 руб.\n"
        "  ашан: 10.99 руб.\n"
        "конфеты:\n"
        "  магнит: 30.99 руб.\n"
        "  пятерочка: 32.99 руб.\n"
    )

    # Вызов функции
    print_prices(sweets)

    # Перехват вывода и проверка
    captured = capsys.readouterr()
    assert captured.out == expected_output, "Функция print_prices работает некорректно"