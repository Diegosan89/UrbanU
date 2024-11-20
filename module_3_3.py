# Распаковка позиционных параметров

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('      task 1')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print('      task 2')
values_list = ['food', True, 451.4]
values_dict = {'a': 78, 'b': 'example', 'c': False}

print_params(*values_list)
print_params(**values_dict)

print('      task 3')
values_list_2 = [125, 'paint']
print_params(*values_list_2, 42)
