# Создание потоков
import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for count in range(1, word_count + 1):
            file.write(f'Какое-то слово № {count}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


functions_started = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
functions_ended = time.time()
print(f'Работа потоков по порядку: {round(functions_ended - functions_started, 2)}')

functions_thread_started = time.time()
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_1.start(), thread_2.start(), thread_3.start(), thread_4.start()
thread_1.join(), thread_2.join(), thread_3.join(), thread_4.join()
functions_thread_ended = time.time()
print(f'Работа потоков по порядку: {round(functions_thread_ended - functions_thread_started, 2)}')
