from functools import reduce
my_list = [el for el in range(100, 1000) if el % 2 == 0]
print(my_list)
mult = reduce((lambda res, x: res*x), my_list)
print(mult)


