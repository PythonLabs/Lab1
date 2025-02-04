# test_shops_logic.py

from shops_logic import get_cheapest_prices

def test_get_cheapest_prices():
    # Входные данные
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
        ],
    }

    # Ожидаемый результат
    expected = {
        'печенье': [
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'ашан', 'price': 10.99},
        ],
        'конфеты': [
            {'shop': 'магнит', 'price': 30.99},
            {'shop': 'пятерочка', 'price': 32.99},
        ],
    }

    # Вызов функции и проверка результата
    result = get_cheapest_prices(shops)
    assert result == expected, "Функция get_cheapest_prices работает некорректно"