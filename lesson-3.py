__author__ = "Nikolay Donetskiy"


# task 1
def div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return None


[a, b] = input("Введите 2 числа, разделенные пробелом> ").split()
result = div(a, b)
if result:
    print(f"{a} / {b} = {result}")
else:
    print("Деление на 0.")


# task 2
def print_user_data(name, surname, year, city, email, phone):
    print(f"Name is {name}, surname is {surname}, birth in {year}, live in {city}, email is {email}, phone is {phone}")


print_user_data(name="Ivan", surname="Ivanov", year="1900", city="Moscow", email="E@mail.com", phone="Cellphone")


# task 3
def my_func(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        num = [a, b, c]
        num.sort(reverse=True)
        return num[0] + num[1]
    except ValueError:
        return None


result = my_func(34, -120, "asd")
if result:
    print(result)


# task 4
def my_func1(x, y):
    try:
        x = int(x)
        y = int(y)
        z = 1
        while y < 0:
            z *= x
            y += 1
        return 1 / z
    except ValueError:
        return None


[x, y] = input("Введите положительное число x и отрицательное число y, разделенные пробелом> ").split()

result = my_func1(x, y)
if result:
    print(f"{x} в степени {y} = {result}")


# task 5

def parse_sum_print(input_string):
    """ Функция извлекает из строки числа, складывает их и выводит результат.


        Использует глобальные переменные:
        summ - глобальная сумма чисел
        exit_flag - флаг завершения работы

    """
    global summ, exit_flag
    elements = input_string.split()
    for i, el in enumerate(elements):
        try:
            f = float(el)
            summ += f
        except:
            if str(el).upper() == "Q":
                print(f"Сумма = {summ}")
                exit_flag = True
                return
    print(f"Сумма = {summ}")
    return


summ = 0
exit_flag = False

while True:
    str_input = input("Введите строку чисел, разделенную пробелами. Введите Q для выхода> ")
    if str_input.upper() == "Q":
        break
    parse_sum_print(str_input)
    if exit_flag:
        break


# task 6

def int_func(s): return str(s).capitalize()


str_input = input("Введите слова, разделенные пробелами> ")
elements = str_input.split()
for el in elements:
    print(int_func(el), end=" ")
