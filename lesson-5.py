__author__ = "Nikolay Donetskiy"

# task 1

with open("task-1.txt", "w") as out_file:
    while True:
        in_s = input("> ")
        out_file.write(in_s + "\n")
        if not in_s:
            break

# task 2
with open("task-1.txt", "r") as in_file:
    for n, i in enumerate(in_file):
        print(f"Line {n + 1} word count = " + str(len(str(i).split())))
    print(f"Lines count = {n + 1}")

# task 3
with open("task-3.txt", "r", encoding="utf_8_sig") as in_file:
    names = ""
    sal_total = 0
    for n, i in enumerate(in_file):
        [fam, sal] = str(i).split()
        sal_total += int(sal)
        if int(sal) < 20000:
            names += str(fam) + ", "
    print(f"Федеральная служба статистики сообщает: средняя заработная плата = {sal_total / (n + 1)}")
    print(f"Заработавшие меншьше 20 000: {names[:-2]}")

# task 4
numbers = [["One", "Один"], ["Two", "Два"], ["Three", "Три"], ["Four", "Четыре"]]

with open("task-4.txt", encoding="utf_8") as in_file:
    alltext = in_file.read()

for [eng, rus] in numbers:
    alltext = alltext.replace(eng, rus)

with open("task-4.txt", "w", encoding="utf_8") as out_file:
    out_file.write(alltext)

# task 5
import random

random.random()
str_numbers = ""
for i in range(random.randint(1, 20)):
    str_numbers += str(random.randint(1, 100)) + " "

with open("task-5.txt", "w") as out_file:
    out_file.write(str_numbers[:-1])
    print(f"{str_numbers}")

with open("task-5.txt", "r") as in_file:
    in_numbers = (in_file.read()).split()

int_summ = 0
for i in in_numbers:
    int_summ += int(i)
print(f"Summ = {int_summ}")

# task 6
with open("task-6.txt", "r", encoding="utf_8") as in_file:
    alltextlines = in_file.readlines()

class_dict = {}
for i in alltextlines:
    class_s = str(i)[:str(i).find(":")]
    int_str = ""
    summ_str = 0
    for si in str(i)[str(i).find(":") + 1:]:
        if si.isdigit():
            int_str += si
        else:
            int_str += " "
    for num_str in int_str.split():
        summ_str += int(num_str)
    class_dict[class_s] = summ_str

print(class_dict)

# task 7
import json

firm_dict = {}
with open("task-7.txt", "r", encoding="utf_8") as in_file:
    for line in in_file:
        line = line.split()
        firm = str(line[0])
        gain = int(line[2]) - int(line[3])
        firm_dict[firm] = gain
    firm_profit_count = 0
    summ_profit = 0
    for ki in firm_dict:
        if firm_dict[ki] > 0:
            firm_profit_count += 1
            summ_profit += firm_dict[ki]
    average_profit = int(summ_profit / firm_profit_count)
    firm_dict["average_profit"] = average_profit

with open("task-7.json", "w") as out_file:
    json.dump(firm_dict, out_file)
