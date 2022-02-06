import json

f = open('seven.txt', 'r')
firms = {}
p_profit = []
for line in f:
    n = line.split()
    name = n[0]
    profit = float(n[2]) - float(n[3])
    firms[name] = profit
    if profit > 0:
        p_profit.append(profit)
avg = sum(p_profit) / len(p_profit)
result = [firms, {'average_profit': avg}]
print(result)
with open('eight.txt', 'w') as new:
    new.write(json.dumps(result))



