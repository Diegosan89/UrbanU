# Очереди для обмена данными между потоками
import threading
import time
from queue import Queue
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    # def __repr__(self):
    #     return f'   {self.number}: {self.guest} - {self.guest.is_alive()}'


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__(None)
        self.name = name

    def __repr__(self):
        return str(self.name)

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            # print(f'    ~берем гостя {guest}')
            for table in self.tables:
                # print(f'        ~берем стол {table.number}')
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest} сел(-а) за стол номер {table.number}')
                    # print(f'      ~~table.guest.is_alive: {table.guest.is_alive()}')
                    break
            # print(f'    ~~гость {guest} статус {guest.is_alive()}')
            if guest.is_alive():
                continue
            self.queue.put(guest)
            print(f'{guest} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(not table.guest is None for table in self.tables):
            # print('~', any(not table.guest is None for table in self.tables))
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest} покушал(-а) и ушёл(ушла).\nСтол номер {table.number} свободен')
                    table.guest = None
                elif table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                else:
                    continue

    # def table_check(self, n):
    #     for i in range(n):
    #         time.sleep(1)
    #         print(f'{self.tables}')


tables_ = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests_ = [Guest(name) for name in guests_names]
cafe = Cafe(*tables_)
cafe.guest_arrival(*guests_)
cafe.discuss_guests()
# cafe.table_check(10)
