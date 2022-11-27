"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    pn = [number ** 2 for number in numbers]
    return pn
print(power_numbers(1,2,5,7))

"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
"""


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(number_list,filter_type):
    if filter_type == ODD:
        return [number for number in number_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in number_list if number % 2 == 0]
    if filter_type == PRIME:
        return[number for number in number_list if 0 not in [number % x for x in range(2,number)] and number > 1]

print(filter_numbers([1,2,3], ODD))
print(filter_numbers([2,3,4,5], EVEN))
print(filter_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], PRIME))
"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""
""