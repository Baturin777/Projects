import copy

data_base_company = {
    'avtopragmat': 4500,
    'gardermag': 3200,
    'akadmig': 2100,
    'aogranted': 3700,
    'promavtomash': 1900,
    'iraero': 2600
}


# первый вариант


# list_dict = list(data_base_company.items())
#
# list_dict.sort(key=lambda i: i[1])

# print(list_dict[-3:])


# Сложность O(NlogN)


# второй вариант


def max_profit(dict_input):

    input_max_profit = {}
    new_dict = copy.copy(dict_input)
    for i in range(3):
        maximum = max(new_dict.items(), key=lambda k_v: k_v[1])
        del new_dict[maximum[0]]
        input_max_profit[maximum[0]] = maximum[1]
    return input_max_profit


print(max_profit(data_base_company))


# Сложность O(N)

# Вывод: Второй вариант решения задачи эффективнее, так как имеет сложность линейной функции O(N), в первом же
# варианте сложность линейно-логорифмической функции O(NlogN)
