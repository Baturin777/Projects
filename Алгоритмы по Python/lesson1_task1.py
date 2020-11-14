# Домашнее задение 1

import random


def check_1(lst_obj):

    """Функция должна создать множество из списка.

        Алгоритм 3:
        Создать множество из списка

        Сложность: O(N).
        """

    lst_to_set = set(lst_obj)   # O(N)
    return lst_to_set


def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

        Алгоритм 1:
        Проходимся по списку и для каждого элемента проверяем,
        что такой элемент отстутствует
        в оставшихся справа элементах

        Сложность: O(n^2)
        """

    for i in range(len(lst_obj)):            # O(n)
        if lst_obj[i] in lst_obj[i + 1:]:    # O(n)
            return False                     # O(1)
    return True                              # O(1)


def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

        Алгоритм 2:
        Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
        Если присутствуют дубли, они будут находиться рядом.

        Сложность: O(N log N)
        """

    lst_copy = list(lst_obj)                 # O(N)
    lst_copy.sort()                          # O(N log N)
    for i in range(len(lst_obj) - 1):        # O(N)
        if lst_copy[i] == lst_copy[i + 1]:   # O(1)
            return False                     # O(1)
    return True                              # O(1)


for j in (50, 500, 1000, 5000, 10000):
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))                     # Домашнее задание 2
