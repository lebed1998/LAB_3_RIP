#!/usr/bin/env python3
from lab_3.librip.gens import gen_random
from lab_3.librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']

# Реализация задания 2
print("Unique(data1) - 1 and 2:                 ", list(Unique(data1)))
print("Unique(data2) - gen_random(1, 3, 10):    ", list(Unique(data2)))
print("Unique(data3) - a, A, b and B:           ", list(Unique(data3)))
print("Unique(data3, ignore_case=True):         ", list(Unique(data3, ignore_case=True)))
