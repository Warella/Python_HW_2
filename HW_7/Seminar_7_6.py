"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""


import os


my_dict = {'jpeg': 'Фото', 'png': 'Фото', 'txt': 'Текст'}


def sort_file(directs: str = 'Test'):
    for file in os.listdir(directs):
        file_exten = file.split('.')[-1]
        if file_exten in my_dict.keys():
            if not os.path.exists(my_dict[file_exten]) or not os.path.isdir(my_dict[file_exten]):
                os.mkdir(my_dict[file_exten])
            os.rename(os.path.join(directs, file), os.path.join(my_dict[file_exten], file))

if __name__ == '__main__':
    sort_file()
