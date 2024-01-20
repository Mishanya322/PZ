class RPA:
 def __init__(self, student, semestr, predmet, attestaciya):
    self.__student = student
    self.__semestr = semestr
    self.__predmet = predmet
    self.__attestaciya = attestaciya
 def get_student(self):
    return self.__student
 def set_student(self, student):
    self.__student = student
 def get_semestr(self):
    return self.__semestr
 def set_semestr(self, semestr):
     self.__semestr = semestr
 def get_predmet(self):
    return self.__predmet
 def set_predmet(self, group):
    self.__predmet = predmet
 def get_attestaciya(self):
    return self.__attestaciya
 def set_attestaciya(self, attestaciya):
    self.__attestaciya = attestaciya
student1 = RPA ('Шишкин',1,{'Математика','Русский Язык'},[5,5])
student2 = RPA('Шадрин', 1, {'Математика', 'Русский Язык'}, [3, 2])
print('Студент: ', student1.get_student())
print('Семестр: ', student1.get_semestr())
print('Предметы: ', student1.get_predmet())
print('Аттестация: ', student1.get_attestaciya())
print('\n')
print('Студент: ', student2.get_student())
print('Семестр: ', student2.get_semestr())
print('Предметы: ', student2.get_predmet())
print('Аттестация: ', student2.get_attestaciya())