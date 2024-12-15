"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from package_lab4.lab2 import task2_1, task2_2, task2_3, task2_4
from package_lab4.lab3 import task3_1, task3_2, task3_3


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """

    choice_lab = int(input('Выберите 2 или 3 лабороторная: '))
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_lab, choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        if choice[0] == 2:

            match choice[1]:

                case 1:
                    a = int(input('Введите первый катет: '))
                    b = int(input('Введите второй катет: '))
                    c = int(input('Введите третий катет: '))
                    task2_1(a, b, c)

                case 2:
                    x = int(input("Введите целое число x: "))
                    print(task2_2(x))

                case 3:
                    x = float(input('Введите x: '))
                    print(task2_3(x))
                case 4:
                    num = int(input('Введите число от 0-9: '))
                    task2_4(num)
                case _:
                    break

        else:
            match choice[1]:

                case 1:
                    print(task3_1())

                case 2:
                    print("Суммарный путь за 7 дней:", task3_2(), "км")

                case 3:
                    x = float(input('Введите x: '))  # значение x, для которого нужно вычислить ln(1 + x)
                    eps = float(input('Введите точность: '))  # заданная точность
                    print(task3_3(x, eps))
                case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

