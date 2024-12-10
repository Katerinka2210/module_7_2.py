def custom_write(file_name, strings): # функция принимает аргументы: название файла для записи
    strings_position = {}
    file = open(file_name, 'w', encoding='utf-8')  # и список строк для записи
    number_string = 1
    for s in strings:
        strings_position[(number_string, file.tell())] = s
        file.write(s + '\n')
        number_string +=1
    file.close()
    return strings_position


info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

