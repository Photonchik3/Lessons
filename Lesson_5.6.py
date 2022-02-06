subj = {}
with open('sixth.txt', 'r') as hours_f:
    for line in hours_f:
        n = line.split()
        subj_name = n[0].strip(':')
        n.pop(0)
        hours_sum = sum([int(x.replace('(л)', '').replace('(лаб)', '').replace('(пр)', '').replace('-', '0')) for x in n])
        subj[subj_name] = hours_sum
print(subj)


