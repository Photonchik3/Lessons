import sys


def salary(hours, sal, bonus):
    pay = hours * sal
    return pay + bonus


print(f'Итого заработная плата : {salary(hours=int(sys.argv[1]), sal=int(sys.argv[2]), bonus=int(sys.argv[3])) }')
