# 20. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

my_list = ["123", "234", 123, "567"]
num = 123

# VAR_1 =========================
for i in range(len(my_list)):
    if my_list[i] == num:
        print(my_list[i], i)


# VAR_2 =========================
if num in my_list:
    print(my_list.index(num))
