#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
# TODO здесь ваш код
print("Все виды цветов:")
all_flowers = garden_set.union(meadow_set)
print(all_flowers)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print("Цветы, которые растут в саду и на лугу")
common_flowers = garden_set.intersection(meadow_set)
print(common_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print("Цветы, которые растут в саду но не на лугу")
garden_only = garden_set.difference(meadow_set)
print(garden_only)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
print("Цветы, которые растут на лугу но не в саду")
meadow_only = meadow_set.difference(garden_set)
print(meadow_only)
