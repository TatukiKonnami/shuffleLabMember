import csv
from lib import member

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