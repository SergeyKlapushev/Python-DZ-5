'''Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел.

2 2
4'''

print('Введите a:')
a = int(input())

print('Введите b:')
b = int(input())
i = 0

def sum(a, b, i):
    if i == b:
        return a + b
    return sum(a, b, i + 1)

print("a + b =", sum(a, b, i))