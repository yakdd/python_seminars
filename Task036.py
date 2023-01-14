# 36. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Вывести все пробелы и их индексы из предыдущей строки. Сделать с помощью filter, lambda

str_1 = 'а абв роза абв, упалаабв на абвлапу азоабвроа'
print(str_1)
lst = str_1.split()

str_2 = ' '.join(list(filter(lambda x: 'абв' not in x, lst)))
print(str_2)

for i, sym in enumerate(str_1):
    if sym == ' ':
        print(i, end=' ')
