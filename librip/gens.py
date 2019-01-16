import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items: list, *args):
    assert len(args) > 0
    single_value = len(args) == 1
    for item in items:
        if single_value:
            x = item[args[0]]
            if x is not None:
                yield item[args[0]]
        else:
            pairs = {key: item[key] for key in dict(item).keys() if key in args}
            if any(x is not None for x in pairs.values()):
                yield pairs


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(0, num_count):
        yield random.randint(begin, end)
