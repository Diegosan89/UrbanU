# Дополнительное практическое задание по модулю

summa = 0

def get_multiplied_digits(*args):
    global summa
    args = list(args)

    if not args:
        return 0

    else:
        elem = args[0]
        if isinstance(elem, str):

            summa += len(elem)

        elif isinstance(elem, int):

            summa += elem

        elif isinstance(elem, tuple) or isinstance(elem, list) or isinstance(elem, set):

            get_multiplied_digits(*elem)

        elif isinstance(elem, dict):

            get_multiplied_digits(*elem.items())

        elem = args.pop(0)

        return summa + get_multiplied_digits(*args)


data = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = get_multiplied_digits(data)
print(result)

