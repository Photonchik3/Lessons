f = open('first.txt', 'w')
data = input('Введите данные: ')
while True:
    line = input('Введите данные: ')
    if line == '':
        break
    data += '\n' + line
f.write(data)

