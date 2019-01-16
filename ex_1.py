#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стеллаж', 'price': 7000, 'color': 'white'},
    {'title': 'Шкаф', 'price': None, 'color': 'white'},             # частично None
    {'title': None, 'price': None, 'color': None}                   # все None
]

# Реализация задания 1
print("field 1:", list(field(goods, 'title123')))
print("field 2:", list(field(goods, 'title', 'price')))
print("gen_random 1:", list(gen_random(1, 3, 5)))
print("gen_random 2:", list(gen_random(1, 3, 5)))