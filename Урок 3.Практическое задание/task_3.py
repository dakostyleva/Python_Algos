"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
import random

array = [random.randint(-100, 100) for i in range(10)]
print(array)

max = max(array)
min = min(array)

print(f'Максимальное число в массиве: {max}')
print(f'Минимальное число в массиве: {min}')

a = array.index(min)
b = array.index(max)

array.remove(min)
array.remove(max)

array.insert(a, max)
array.insert(b, min)

print(f"Новый массив: {array}")
