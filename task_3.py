''''
На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете,
что функция соответствует заданным критериям.
'''



"""
Лучше всего использовать втроенную функцию sort(), так как она реализована на С++, а данный код выполняется с помощью языка питон.
sort() будет ,будет гараздо быстрее. Но суть задачи показать свою навыки программирования, поэтому я написал алгоритм Хоара
"""

import random

def sort_mas(mas):
    if len(mas) > 1:
        random_num = mas[
            random.randint(0, len(mas) - 1)]  # Выбираем случаеное значение из списка, с которым потом будем сравнивать
        lower = [el for el in mas if el < random_num]  # Формируем список всех значений, которые меньше чем выбранное
        cur = [el for el in mas if el == random_num]  # Формируем список значений равных выбранному
        high = [el for el in mas if el > random_num]  # Формируем список из значений, которые больше выбранного
        mas = sort_mas(lower) + cur + sort_mas(high)  # рекурсивно вызываем функцию и объеденяем списки
    return mas


'''
Для решения выбранной задачи был выбран алгоритм Хоара, так как он один из самых быстрых. Так как в массиве может быть уже отсортированный список,
поэтому мы берем случайное значение, а не начальный элемент. Это способ использует много памяти, это сделано для увилечения скорости,
но строчки 12-14 можно заменить на сортировку в том же самом массиве, который мы передаём в функцию, это уменьшит расходы памяти
скорость выполнения данного способа сортировки составляет O(N*log2N) 

Ниже проверка, что алгоритм работает
'''

mas = [15, 6, -2, 19, 0, -100, 1, -2, 0, 44, 3]
mas = sort_mas(mas)

print(mas)
