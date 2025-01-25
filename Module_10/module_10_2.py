# Потоки на классах
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__(None)
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.enemy:
            time.sleep(1)
            day += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {day} дней, осталось {self.enemy} воинов.')

        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')