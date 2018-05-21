from enum import Enum
class Grade(enum):
    MASTER = 1
    BACHELOR = 2
    ATHOR = 3

    def setGrade(self, grade):
        if grade == 'M':
            return Grade.MASTER
        elif grade == 'B':
            return Grade.BACHELOR
        elif grade == 'A':
            return Grade.ATHOR

class Member():
    NAME = ''
    GRADE = Grade()

    def setData(self, name, grade):
        self.NAME = NAME
        self GRADE.setGrade(grade)

    def toString(self):
        print('Name : ' + self.NAME + '\nGrade : ' + self.GRADE)
