# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

all_coins = int(input('Введите количество монет: '))
import random
list_1 = []
for i in range(all_coins):
    i = random.randint(1, 2)
    list_1.append(i)
print(list_1)

eagle = 0
for i in list_1:
    if i != 2:
        eagle = eagle + 1

print(f'Орлом выпало:  {eagle}')
print(f'Решкой выпало:  {all_coins - eagle}')

if eagle < all_coins/2:
    print(f"Нужно перевернуть: {eagle} монеток")
else:
    print(f"Нужно перевернуть: {all_coins - eagle} монеток")
