# Реализуйте алгоритм перемешивания списка.
from random import randint
import random

# lst = list(range(1, 15, 3))
# print(lst)
# random.shuffle(lst)
# print(lst)


new_list = []
rnd = randint
for i in range(0, 10):
    number = rnd(1, 50)
    new_list.append(number)
print(new_list)

list = new_list[:]
    
list_length = len(list)
for i in range(list_length):        
    rand = random.randint(0, list_length - 1)
    
    temp = list[i]
    list[i] = list[rand]
    list[rand] = temp

print(list)



