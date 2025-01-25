# Блокировки и обработка ошибок

import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.depo_transaction_counter = 0

    def deposit(self):
        for transaction in range(100):
            self.depo_transaction_counter += 1
            value = random.randint(50, 500)
            self.balance += value
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {value}. Баланс: {self.balance}.')
            time.sleep(0.0000001)

    def take(self):
        take_transaction_counter = 0
        for transaction in range(100):
            take_transaction_counter += 1
            value = random.randint(50, 500)
            print(f'Запрос на {value}.')
            if value <= self.balance:
                self.balance -= value
                print(f'Снятие: {value}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                if self.depo_transaction_counter == 100:
                    print('Bank out of balance!')
                    break
            #print(f'    Сделано пополнений: {self.depo_transaction_counter}, списаний: {take_transaction_counter}')
            time.sleep(0.00001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}.')
