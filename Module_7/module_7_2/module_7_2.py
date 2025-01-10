# Позиционирование в файле

def custom_write(file_name, strings):
    string_number = 0
    dict = {}
    for string in strings:
        file = open(file_name, 'a', encoding='utf-8')
        string_number += 1
        begin_byte = file.tell()
        file.write(f'{string}\n')
        dict.update({(string_number, begin_byte): string})
        file.close()
    return dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('module_7_2.txt', info)
for elem in result.items():
    print(elem)

