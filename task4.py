# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint


n = int(input('Введите число: '))

n_list = []

rnd = randint
for i in range(0, n):
    number = rnd(-n, n)
    n_list.append(number)
print(n_list)

index = (input('Введите индекс элементов через пробел: ').split(' '))
print(index)
mult = 1
for i in range(0,len(index)):
    mult *= n_list[int(index[i])]
 

print(f'Произведение указанных элементов: {mult}')

