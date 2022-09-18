from .store import Store


class Shop(Store):
    def __init__(self, items: dict = {}):
        self._items = items
        self._max_items_values = 5
        self._capacity = 5

    def add(self, name, count):
        if self._get_free_space() < count:
            return 'В магазине недостаточно места'

        if name in self._items:
            self._items.update({name: self._items.get(name) + count})
        elif self._get_unique_items_count() < self._max_items_values:
            self._items.update({name: count})
        else:
            return "В магазине отсутствует место для новой позиции"

    def remove(self, name, count):
        if name not in self._items:
            return 'Нужного товара нет в магазине'

        if (item_count := self._items.get(name)) >= count:
            self._items.update({name: item_count - count})
        else:
            return 'Товара в таком количестве в магазине нет'
