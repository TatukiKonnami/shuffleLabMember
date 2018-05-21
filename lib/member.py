from enum import Enum
class Grade(Enum):
    MASTER = 'M'
    BACHELOR = 'B'
    ATHOR = 'A'

    def setGrade(self, grade):
        if grade == 'M':
            return Grade.MASTER
        elif grade == 'B':
            return Grade.BACHELOR
        elif grade == 'A':
            return Grade.ATHOR
    


class Member():
    NAME = ''
    GRADE = Grade('A')
    ORGANIZE = 0

    def setData(self, name, grade, organize):
        self.NAME = name
        self.GRADE = Grade('A').setGrade(grade)
        self.ORGANIZE = organize

    def toString(self):
        print('Name : ' + self.NAME + ' Grade : ' + self.GRADE.name)
