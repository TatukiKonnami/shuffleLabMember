import member
import csv
import random

data = []
print('scan csv file.')
path = input()
f = open(path,'r')
itr = 1

r = csv.DictReader(f)

for row in r:
    names = row.keys()
    name = names[0]
    grade = row[name]
    member = Member()
    member.setData(name, grade)
    data.append(member)

random.shuffle(data)

for i in data:
    print(itr)
    i.toString()
    itr = itr + 1
