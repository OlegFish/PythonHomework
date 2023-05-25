"""
Задача 2: Найдите сумму цифр трехзначного числа.
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 
"""

#задача 2
sum = 0
a = int(input('Ведите число: '))
while a > 0:
    sum += a % 10
    a //= 10
print('Сумма цифр числа ', sum)

#задача 4
s = int(input('\nВведите S: '))
if s % 6 == 0:
    x = s // 6
    print(f"Петя {x}, Катя {x*4}, Сережа {x}")
else:
    print('Задача не имеет решения ')

#задача 6
ticket = int(input('\nВведите шестизначный номер билета: '))
left_sum = ticket // 100000
ticket %= 100000
left_sum += ticket // 10000
ticket %= 10000
left_sum += ticket // 1000
ticket %= 1000

right_sum = ticket // 100
ticket %= 100
right_sum += ticket // 10
ticket %= 10
right_sum += ticket

if left_sum == right_sum:
    print('yes')
else:
    print('no')

#задача 8
n = int(input('\nВведите n: '))
m = int(input('Введите m: '))
k = int(input('Введите k: '))

if (((n * m - k) % n) == 0 and (k % n == 0)) or (((n * m - k) % m) == 0 and (k % m == 0)):
    print('yes')
else:
    print('no')

