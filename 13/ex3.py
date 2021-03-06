import holidays
import datetime

class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()
    
    @property
    def email(self):
        return '{}.{}@university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, new_avg):
        cls.min_avg = new_avg

    @staticmethod
    def academic_footbal_team_cheer(no):
        return "Go go NYA! " * no

    @staticmethod
    def academic_day(day):
        pl_holidays = holidays.Polish()
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Nie'
        elif datetime.date.today() in pl_holidays == True:
            return 'Nie'
        else:
            return 'Tak'

today = datetime.date.today()

print('Czy dzisiaj są zajęcia? ', Student.academic_day(today))

print(today, 'zajęcia się odbywają:', Student.academic_day(today))

kroli3 = datetime.datetime.strptime('2019-01-06', '%Y-%m-%d')
print(kroli3, 'zajęcia się odbywają:', Student.academic_day(kroli3))


obj_anna = Student("Anna", "kowalska", 23, 4.7)
obj_arek = Student("Arek", "Nowak", 21, 3.9)

print(obj_anna.min_avg)
print(obj_arek.min_avg)

obj_anna.set_min_avg(3.0)
print(obj_anna.min_avg)
print(obj_arek.min_avg)
print(Student.academic_footbal_team_cheer(4))
print(obj_anna.email)