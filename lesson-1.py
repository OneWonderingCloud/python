__author__ = "Nikolay Donetskiy"

#task 2
seconds = int(input("Please input time in seconds: "))
# not optimized but quite straightforward)
print(f"Time is {seconds // 3600} hour(s) {(seconds % 3600) // 60} minute(s) and {seconds % 60} second(s)")

# task 3
n = int(input("Please input number n: "))
while n < 0:
    n = int(input("n must be >= 0. Please input number n: "))
print(f"{n} + {str(n) + str(n)} + {str(n) + str(n) + str(n)} = {n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))}")

# task 4
n = int(input("Please input number n: "))
max_digit = 0
while n > 0:
    modulo = n % 10
    if modulo > max_digit:
        max_digit = modulo
    n = n // 10
print(f"Biggest digit in n = {max_digit}")

# task 5
earnings = float(input("Please input earnings: "))
expenses = float(input("Please input expenses: "))
gain = earnings - expenses
if gain > 0:
    print(f"You have a profit = {gain}. Profitability = {earnings / gain}")
    emp_count = int(input("Please input employee count: "))
    print(f"Profit per imployee = {gain / emp_count}")
else:
    print(f"You only have a loss = {gain}.")

# task 6
a = int(input("Input a: "))
b = int(input("Input b: "))

n = 1
while a <= b:
    a = a * 1.1
    n += 1
print(n)
