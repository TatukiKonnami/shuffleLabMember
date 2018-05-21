from lib import member
from lib import memberList as l
import csv
import random


data = []
shuffledata = []
itr = 1

f = open('out.txt','w')

print('scan csv file.')
path = input()
data = l.readCSV(path)

print('what is the purpose?(Organize decision -> OD | Sort)')
purpose = input()
if purpose == 'OD':
    shuffledata = l.decision(data)
elif purpose == 'Sort':
    shuffledata = l.sort(data)
else:
    print('retry')

random.shuffle(shuffledata)

for i in shuffledata:
    print(itr)
    print(i.toString())
    f.write(i.toString() + '\n')
    itr = itr + 1
f.close()