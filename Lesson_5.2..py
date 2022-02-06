f = open('second.txt', 'r')

line_cnt = 0

for line in f:
    line_cnt += 1
    word_cnt = len(line.split())
    print('строка {} содержит {} слов'.format(line_cnt, word_cnt))

print('Всего {} строк в файле'.format(line_cnt))


