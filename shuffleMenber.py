from lib import member
import csv
import random

def readCSV(path):
    data = []

    f = open(path,'r')

    r = csv.DictReader(f)

    for row in r:
        print(type(row), row)
        name = row['Name']
        grade = row['grade']
        org = row['organize']
        a_member = member.Member()
        a_member.setData(name, grade, org)
        data.append(a_member)
    
    return data

def decision(data):
    shuffledata = []

    for i in data:
        if i.ORGANIZE == '0':
            shuffledata.append(i)
    
    return shuffledata

def sort(data):
    shuffledata = []
    exceptGrade = []

    print('except grade (M, B, A)')
    ex = input()
    try:
        ed = ex.split(' ')
        for e in ed:
            eg = member.Grade("A").setGrade(str(e))
            exceptGrade.append(eg)
        for i in data:
            if i.GRADE not in exceptGrade:
                shuffledata.append(i)
    except:
        shuffledata = data

    return shuffledata

data = []
shuffledata = []
itr = 1

print('scan csv file.')
path = input()
data = readCSV(path)

print('what is the purpose?(Organize decision -> OD | Sort)')
purpose = input()
if purpose == 'OD':
    shuffledata = decision(data)
elif purpose == 'Sort':
    shuffledata = sort(data)
else:
    print('retry')



random.shuffle(shuffledata)

for i in shuffledata:
    print(itr)
    i.toString()
    itr = itr + 1
