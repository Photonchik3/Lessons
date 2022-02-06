f = open('fourth.txt', 'r')
rus = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
ru_list = []
for line_en in f:
    n = line_en.split('-')[1].strip()
    line_ru = rus[n] + ' - ' + n + '\n'
    ru_list.append(line_ru)

f_ru = open('fourth_1.txt', 'w')
f_ru.writelines(ru_list)



