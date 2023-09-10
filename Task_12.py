# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#  Помогите Кате отгадать задуманные Петей числа.

import random
from math import sqrt

x = random.randint(1, 1001)
y = random.randint(1, 1001)
print(x)
print(y)

S = x + y
P = x * y
y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1, y1)

# my_list = []
# for _ in range(s):
#     my_list.append(_)
# print(my_list)

# def find_num1(n, list):
#     for i in list:
#         res = i * list[-1]
#         if res == n:
#             return res
#         return find_num1(n, list.pop())
# print(find_num1(p, my_list)) 

    # else:    
    #     print(my_list[-1])
    #     print(s - my_list[0])
        
    # if res != p:
    #     my_list.pop()
    #     continue

# for i in my_list:
#     res = i * my_list[-1]
#     i += 1
#     if res != p:
#         my_list.pop()     
#     else:
#         print(my_list(-1))
#         print(f'y = {res/my_list(-1)}')
    





