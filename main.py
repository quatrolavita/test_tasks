from itertools import permutations


def slice_less(my_list: list, lesser: int) -> list:
    """ in this task i use list comprehension"""

    return [item for item in sorted(my_list, reverse=True) if item > lesser]


def biggest_value(my_list: list) -> int:
    """ in this task i use itertools with permutations and some type conversion"""

    max_val = 0

    for i in permutations(my_list, len(my_list)):

        c = int(''.join(list(map(str, i))))

        if c > max_val:
            max_val = c

    return max_val
