#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
# table_code = goods['Стол']
# table_items = store[table_code]
# table_quantity = sum(item['quantity'] for item in table_items)
# table_cost = sum(item['quantity'] * item['price'] for item in table_items)
# print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

table_code = goods['Стол']
table_items = store[table_code]
table_quantity = table_items[0]['quantity'] + table_items[1]['quantity']
table_cost = (table_items[0]['quantity'] * table_items[0]['price']) + (table_items[1]['quantity'] * table_items[1]['price'])
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

sofa_code = goods['Диван']
sofa_items = store[sofa_code]
sofa_quantity = sofa_items[0]['quantity'] + sofa_items[1]['quantity']
sofa_cost = (sofa_items[0]['quantity'] * sofa_items[0]['price']) + (sofa_items[1]['quantity'] * sofa_items[1]['price'])
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chair_items = store[chair_code]
chair_quantity = chair_items[0]['quantity'] + chair_items[1]['quantity'] + chair_items[2]['quantity']
chair_cost = (chair_items[0]['quantity'] * chair_items[0]['price']) + (chair_items[1]['quantity'] * chair_items[1]['price']) + (chair_items[2]['quantity'] * chair_items[2]['price'])
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')