from typing import Optional

from .store import Store
from .shop import Shop


class RequestWorker:
    def __init__(self, stores: list[Store, Shop]):
        self._store = stores[0]
        self._shop = stores[1]
        self._request: str

        self._amount: int
        self._product: str
        self._from_str: str
        self._to_str: str
        self._from: Optional[Store, Shop]
        self._to: Optional[Store, Shop]
        self._announce()

    def _announce(self):
        print("=======\nВ складе хранится:")
        print(self._store.get_items())
        print("\nВ магазине хранится:")
        print(self._shop.get_items())
        print("=======\n")

    def _parse(self):
        splitted = self._request.lower().split()
        self._amount, self._product, self._from_str, self._to_str = int(splitted[1]), splitted[2], splitted[4], splitted[6]

    def _validate(self):
        if self._from_str == 'магазин':
            self._from = self._shop
            self._to = self._store
        else:
            self._from = self._store
            self._to = self._shop

    def accept_request(self, request):
        self._request = request
        self._parse()
        self._validate()
        self._do_work()
        self._end_announce()

    def _end_announce(self):
        print("\nВ складе хранится:")
        print(self._store.get_items())
        print("\nВ магазине хранится:")
        print(self._shop.get_items())

        print('=======\n')

    def _do_work(self):
        print(f"Курьер приехал забрать {self._amount} {self._product} из/со {self._from_str}")
        if msg := self._from.remove(self._product, self._amount):
            print("Курьера развернули и сказали ", msg)
            return
        print(f"Курьер забрал и повез {self._amount} {self._product} в/на {self._to_str}")
        print(f"Курьер привез {self._amount} {self._product} в/на {self._to_str}")
        if msg := self._to.add(self._product, self._amount):
            print("Курьера развернули, и сказали ", msg)
            print("Курьера приехал обратно, и вернул товар")
            self._from.add(self._product, self._amount)
            return
        else:
            print("Курьер завершил заказ")
