# Многопроцессное программирование
import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            our_line = file.readline()
            all_data.append(our_line)
            if not our_line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = time.time()
# for filename in filenames:
#     read_info(filename)
# end = time.time()
# print(round(end - start, 4))


if __name__ == '__main__':
    start = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
    end = time.time()
    print(round(end - start, 4))
