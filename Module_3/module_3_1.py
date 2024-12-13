# Пространство имён

calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    presence = string.lower() in [str.lower(i) for i in list_to_search]
    return presence

print('urban' == 'URban')

print(string_info('Lamborgini'))
print(string_info('depositariy :)'))
print(is_contains('Jeep', ['LADA', 'BMW', 'Opel']))
print(is_contains('apPle', ['LEMON', 'Pinapple', 'ApplE']))
print(calls)