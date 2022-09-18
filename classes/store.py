from .aclass import StorageBase


class Store(StorageBase):
    def __init__(self, items: dict = {}):
        self._items = items
        self._capacity = 100

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, name, count):
        if self._get_free_space() < count:
            return 'На складе недостаточно места, попробуйте что то другое'

        if name not in self._items:
            self._items.update({name: count})
        else:
            self._items.update({name: self._items.get(name) + count})

    def remove(self, name, count):
        if name not in self._items:
            return 'Нужного товара нет на складе'

        if (item_count := self._items.get(name)) >= count:
            self._items.update({name: item_count - count})
        else:
            return 'Товара на складе не достаточно'

    def _get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def _get_unique_items_count(self):
        return len(self._items.keys())
