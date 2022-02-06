f = open('fifth.txt', 'w')
f.write(str('1 2 8 3 5 6'))

with open('fifth.txt', 'r') as f:
    my_list = f.read().split()
    result = sum(map(int, my_list))
print(result)

