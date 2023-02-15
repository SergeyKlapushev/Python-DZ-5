'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

print('Введите число:')
a = int(input())

print('Введите степень:')
b = int(input())

def degree (a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        return (a * degree(a, b-1))

print(degree(a, b))