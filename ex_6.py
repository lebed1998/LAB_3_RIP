#!/usr/bin/env python3
import json
import sys
from lab_3.librip.ctxmngrs import timer
from lab_3.librip.decorators import print_result
from lab_3.librip.gens import field, gen_random
from lab_3.librip.iterators import Unique

if len(sys.argv) < 2:
    print("Нужно указать параметр пути к файлу")
    exit(1)

path = sys.argv[1]

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


@print_result
def f1(arg):
    return list(sorted(Unique(field(arg, 'job-name'), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda x: str(x).lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: '{} с опытом Python'.format(x), arg))


@print_result
def f4(arg):
    salaries = list(gen_random(100000, 200000, len(arg)))
    result = map(lambda x: "{}, зарплата {} руб.".format(x[0], x[1]), zip(arg, salaries))
    return list(result)


with timer():
    f4(f3(f2(f1(data))))

