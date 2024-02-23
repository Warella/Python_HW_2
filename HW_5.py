import os


# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def get_path(path):
    last_symbol = path.rfind('/')
    file_path = path[:last_symbol]
    last_dot = path.rfind('.')
    if last_dot == -1:
        file_name = path[last_symbol+1:]
        extension = ''
    else:
        file_name = path[last_symbol+1:last_dot]
        symbol = path[last_dot+1:]
    return file_path, file_name, extension

# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Анна", "Юрий", "Виктория"]
salaries = [40000, 75000, 200000]
bonuses = ["10.25%", "15.50%", "20.75%"]

salary_dict = generate_salary_dict(names, salaries, bonuses)
print(salary_dict)

# 4. Создайте функцию генератор чисел Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b