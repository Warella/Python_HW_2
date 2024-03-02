"""Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""


from Seminar_7_3 import gen_name
import random
import os


def gen_file(exten: str, directs: str, min_len: int = 6, max_len: int = 30,
             min_bytes: int = 256, max_bytes: int = 4096,
             num_files: int = 42):
    if not os.path.exists(directs) or not os.path.isdir(directs):
        os.mkdir(directs)
    for i in range(num_files):
        while True:
            name = gen_name(random.randint(min_len, max_len))
            if name + exten not in os.listdir(directs):
                break
        bytes = gen_name(random.randint(min_bytes, max_bytes))
        with open(directs + '/' + name + exten, 'w', encoding='utf-8') as f:
            f.write(bytes)


if __name__ == '__main__':
    gen_file('.mrk', directs = 'Test', num_files=4)