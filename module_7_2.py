

def custom_write(file_name, string):
    string_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    number = 1
    for string in string:
        string_position[(number, file.tell())] = string
        file.write(string + '\n')
        number += 1
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
