# В Python встроена функция filter https://book.pythontips.com/en/latest/map_filter.html
# Используя yield/yield from необходимо реализовать свою функцию _filter, которая будет делать то же самое.
# number_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

# -------------------------------------------------------------------------------------------------------------


def gen_1(x):
    for i in x:
        if i < 0:
            yield i


limit = range(-5, 5)
result_1 = list(gen_1(limit))
print(result_1)

# _____________________________________________________________________________________________________________


def gen_2(x):
    yield from (i for i in x if i < 0)


result_2 = list(gen_2(limit))
print(result_2)
