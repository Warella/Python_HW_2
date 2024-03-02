from random import random, randint, choice


# 1. Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

"""def rand_num(lines: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        num1 = randint(-1000, 1000)
        num2 = random() * 2000 - 1000
        for i in range(lines):
            print(f'{num1} | {num2}', file=f, end='\n')

if __name__ == '__main__':
    rand_num(100, file_name='Seminar.txt')"""

# 2. Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные. Полученные имена сохраните в файл.

VOWLES = ['a', 'o', 'u', 'e', 'i', 'y']

def gen_name():
    length = randint(4, 7)
    min_letter = ord('a')
    max_letter = ord('z')
    names = []
    for _ in range(length):
        names.append(chr(randint(min_letter, max_letter)))
    flag = False
    for letter in names:
        if letter in VOWLES:
            flag = True
            break
    if not flag:
        i = randint(0, length - 1)
        letter = choice(VOWLES)
        names[i] = letter
    names = ''.join(names).capitalize()
    return names


def file_names(lines: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(lines):
            f.write(f'{gen_name()}\n')

if __name__ == '__main__':
    file_names(15, '../names.txt')

# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.