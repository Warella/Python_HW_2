import os

# Задача 1. Напишите функцию для транспонирования матрицы

def trans_matrix(matrix):
    trans_m = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_m


print(trans_matrix([[1, 2, 3], [4, 5, 0]]))

# Задача 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def func_key(**kwargs):
    return {v if v.__hash__ is not None else str(v):k for k, v in kwargs.items()}


print(func_key(arg1="Hello", arg2=2, arg3="123", arg4=[1, 2, 3, 4, 5]))

# Задача 3. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def menu():
    balance = 0
    count = 0
    operation_list = []
    print('Добро пожаловать!')
    while True:
        while True:
            command = input('Выберите действие: \n '
                            '1 - пополнить\n'
                            '2 - снять\n'
                            '3 - выйти\n')
            if command not in ('1', '2', '3'):
                print('Выберите действие заново')
            else:
                break
        match command:
            case '1':
                balance, count = replanish(balance, count)
                operation_list += 'Пополнение на сумму' + {balance}
                print(f'Ваш баланс: {balance}')
            case '2':
                balance, count = withdraw(balance, count)
                operation_list += 'Снятие на сумму' + {balance}
                print(f'Ваш баланс: {balance}')
            case '3':
                print(f'Ваш баланс: {balance}\n '
                      f'До свидания!')
                break
def replanish(balance, count):
    if balance > 5000000000:
        balance *= 0.9
    while True:
        try:
            start_sum = int(input('Введите сумму пополнения, кратную 50: '))
        except:
            exit_option = int(input('Введите 0, чтобы выйти в главное меню: '))
            if exit_option == 0:
                return balance, count
            else:
                continue
        if start_sum % 50 == 0:
            break
    balance += start_sum
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    return balance, count

def withdraw(balance, count):
    if balance > 5000000000:
        balance *= 0.9
    while True:
        try:
            start_sum = int(input('Введите сумму снятия, кратную 50: '))
        except:
            exit_option = int(input('Введите 0, чтобы выйти в главное меню: '))
            if exit_option == 0:
                return balance, count
            else:
                continue
        if start_sum % 50 == 0:
            perc = start_sum * 1.015
            if perc < 30:
                perc = 30
            elif perc > 600:
                perc = 600
            if start_sum + perc > balance:
                print('Недостаточно средств')
                continue
            else:
                break
    balance -= (start_sum + perc)
    balance += start_sum
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    return balance, count

if __name__ == '__main__':
    menu()
