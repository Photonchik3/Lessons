def my_pow1(x, y):
    return x ** y


def my_pow2(x, y):
    result = x
    for i in range(abs(y)-1):
        result = result * x
    return 1 / result


n1 = abs(float(input('Введите действительное положительное число ')))
n2 = abs(int(input('Введите целое отрицательное число '))) * -1
print(my_pow1(n1, n2))
print(my_pow2(n1, n2))



