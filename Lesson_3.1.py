def divide(n1, n2):
    while n2 == 0:
        n2 = int(input('На ноль делить нельзя, введите другое число '))
    return n1/n2


p1 = int(input('Ведите первое число '))
p2 = int(input('Ведите второе число '))
print(divide(p1, p2))


