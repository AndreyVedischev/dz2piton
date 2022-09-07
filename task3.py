# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input('Введите колличество чисел в последовательности: '))

k_list = []

for i in range(1, k + 1):
    number = float((1 + 1/i)**i)
    k_list.append(number)
print(k_list)

sum = 0
for i in k_list:
    sum += i

print('Сумма чисел последовательности равна:', sum)
