"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона."""

import random


def gen_name(num_char: int) -> str:
    list_name = []
    for i in range(num_char):
        list_name.append(chr(random.randint(ord('a'), ord('z'))))
    return ''.join(list_name)

def gen_file(exten: str, min_len: int = 6, max_len: int = 30,
             min_bytes: int = 256, max_bytes: int = 4096,
             num_files: int = 42):
    for i in range(num_files):
        name = gen_name(random.randint(min_len, max_len))
        bytes = gen_name(random.randint(min_bytes, max_bytes))
        with open('Test/' + name + exten, 'w', encoding='utf-8') as f:
            f.write(bytes)

if __name__ == '__main__':
    gen_file('.txt', num_files=4)