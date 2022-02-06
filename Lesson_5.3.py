f = open('third.txt', 'r')
employee = {}
for line in f:
    a = line.split()
    fullname = a[0]
    sal = float(a[1])
    employee[fullname] = sal
    if sal < 20000:
        print(fullname)

avg = sum(employee.values())/len(employee)
print(avg)