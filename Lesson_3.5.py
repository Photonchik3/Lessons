number_sum = 0
is_stopped = False
while not is_stopped:
    n = input('Введите строку чисел с пробелом: ')
    str_list = n.split()
    number_list = []
    for x in str_list:
        if x.isdigit():
            number_list.append(int(x))
        else:
            is_stopped = True
            break
    number_sum = number_sum + sum(number_list)
    print(number_sum)
