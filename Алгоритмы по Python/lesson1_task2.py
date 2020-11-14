import random

lst = [random.randint(0, 50) for i in range(10)]

print(lst)

#второй вариант

min_elem = lst[0]
for i in range(1, len(lst)):
    if lst[i] < min_elem:
        min_elem = lst[i]
print(min_elem)

#первый вариант

min_elem = lst[0]
for i in lst:
    for j in lst:
        if i >= min_elem > j:
            min_elem = j

print(min_elem)








