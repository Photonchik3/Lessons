def my_func(p1, p2, p3):
    return p1 + p2 + p3 - min(p1, p2, p3)


n1 = int(input('Введите 1-е число: '))
n2 = int(input('Введите 2-е число: '))
n3 = int(input('Введите 3-е число: '))
print(my_func(n1, n2, n3))
