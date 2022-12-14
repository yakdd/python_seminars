# 7. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

bool_list = [0, 1]

print('x y z\t| left right\t| result')
print('--------+---------------+------')

for x in bool_list:
    for y in bool_list:
        for z in bool_list:
            left = not (x or y or z)
            right = not x and not y and not z
            print(x, y, z, end='\t| ')
            print(left, right, end='\t| ')
            print(left == right)
