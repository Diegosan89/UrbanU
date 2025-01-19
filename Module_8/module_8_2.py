# Сложные моменты и исключения в стеке вызовов функции
from _operator import countOf


def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы: {number} - {type(number)}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        summa = personal_sum(numbers)[0] # ДЛЯ СЕБЯ: НЕ называть переменную именем встроенной функции (sum)!
        result = summa / countOf(map(type, numbers), int)
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        result = None
    return result


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
