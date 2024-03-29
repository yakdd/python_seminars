# 39(1). Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом,
# вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой.
# В конце вывести игрока, который победил.
# Условие задачи:
# На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# В качестве дополнительного усложнения можно:
# a) Добавьте игру против бота (где бот берет рандомное количество конфет от 0 до 28)
# b) Подумайте как наделить бота 'интеллектом' (есть алгоритм, позволяющий выяснить
#    какое количесвто конфет необходимо брать, чтобы гарантированно победить,
#    соответственно внедрить этот алгоритм боту )


# Игра для двух человек:
from random import randint


def move(tot, lim, pl_1):
    player = 'Игрок_1' if pl_1 else 'Игрок_2'
    if tot <= lim:
        print(f'\t{player} забирает оставшиеся {tot} конфет и побеждает!')
        return 0
    while True:
        take = int(input(f'\t{player}, возьмите не более 28 конфет: '))
        if 1 <= take <= lim:
            tot -= take
            break
        print('НЕВЕРНОЕ ЧИСЛО!')
    return tot


def fate():
    lot = randint(1, 2)
    if lot == 1:
        return 'player_1'
    return 'player_2'


total = 221
limit = 28

first_player = fate()
if first_player == 'player_1':
    player_1 = True
    player_2 = False
    first = player_1
else:
    player_1 = False
    player_2 = True
    first = player_2

print('=== ИГРА С КОНФЕТАМИ ДЛЯ ДВУХ ЧЕЛОВЕК ===')
print(f'Количество конфет - {total}. За один ход можно забрать не более чем {limit} конфет.')
while total:
    print(f'Остаток конфет: {total}')
    total = move(total, limit, player_1)
    if total:
        player_1, player_2 = player_2, player_1
