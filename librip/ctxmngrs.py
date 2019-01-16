# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

from contextlib import contextmanager
import time


@contextmanager
def timer():
    before = time.time()
    yield
    delta = time.time() - before
    print("{} s".format(delta))
