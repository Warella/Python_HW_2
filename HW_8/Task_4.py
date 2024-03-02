"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV."""

with open('result1.csv', 'w', encoding='utf-8') as csv_file:
    for key, value in access_dict.items():
        for key2, value2 in value.items():
            csv_file.write(f'{key},{key2},{value2}\n')