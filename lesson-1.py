__author__ = "Nikolay Donetskiy"

# task 3
n = int(input("Please input number n:"))
while n < 0:
    n = int(input("n must be >= 0. Please input number n:"))
print(
    f"{n} + {str(n) + str(n)} + {str(n) + str(n) + str(n)} = {n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))}")


# task 4
max_digit = 0
while n > 0:
    modulo = n % 10
    if modulo > max_digit:
        max_digit = modulo
    n = n // 10
print(f"Max digit in n = {max_digit}")


# task 6
a = int(input("Input a:"))
b = int(input("Input b:"))

n = 1
while a <= b:
    a = a * 1.1
    n += 1
print(f"{n} days")
