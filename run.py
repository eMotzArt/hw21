from classes import Store
from classes import Shop
from classes import RequestWorker

if __name__ == '__main__':
    items = {
        'печеньки': 15,
        'собачки': 10,
        'яблоки': 20,
        'лампочки': 2,
    }

    store = Store(items)
    shop = Shop()
    request_worker = RequestWorker([store, shop])

    while True:
        request_worker.accept_request(input('Введите команду следующего формата:\nДоставить 3 собачки из склад в магазин\n>>> '))
