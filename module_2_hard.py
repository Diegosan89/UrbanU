# Дополнительное практическое задание по модулю: "Основные операторы"

n = int(input('Введите число из первого поля: '))

list_ = ''
for i in range(1, n):
    for j in range(i+1, n):
        if n % (i + j) == 0:
            list_ += (f'{i}{j}')
    if i >= (n // 2):             # для сокращения перебора так как новые числа всё равно не добавятся
        break

print('Пароль: ', list_)