from lib import member
from lib import memberList as l
import csv
import random

data = []
shuffledata = []
itr = 1

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
    i.toString()
    itr = itr + 1
