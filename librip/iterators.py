# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):            # kwargs => ignore_case: Bool
        self._items = list(items)
        self._uniques = set()
        self._index = 0
        self._ignore_case = kwargs.pop('ignore_case', False)
        pass

    def process_item_ignore_case(self, item):
        if isinstance(item, str) and self._ignore_case:
            return str(item).lower()
        else:
            return item

    def remember_having(self, item):
        self._uniques.add(self.process_item_ignore_case(item))

    def happen_to_have(self, item):
        return self.process_item_ignore_case(item) in self._uniques

    def __next__(self):
        length = len(self._items)
        while self._index < length:
            current = self._items[self._index]
            if not self.happen_to_have(current):
                self.remember_having(current)
                return current
            else:
                self._index += 1
        raise StopIteration

    def __iter__(self):
        return self
