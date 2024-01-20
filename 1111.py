class RPA:
    def __init__(self, familiya, imya, semestr, predmet, attestaciya):
        self.__familiya = ""
        self.__imya = ""
        self.set_familiya(familiya)
        self.set_imya(imya)
        self.__semestr = int(semestr)
        self.__predmet = predmet
        self.__attestaciya = attestaciya

    def get_familiya(self):
        return self.__familiya

    def set_familiya(self, familiya):
        self.__familiya = ''.join(c for c in familiya if c.isalpha() or c == "-")

    def get_imya(self):
        return self.__imya

    def set_imya(self, imya):
        self.__imya = ''.join(c for c in imya if c.isalpha() or c == "-")

    def get_semestr(self):
        return self.__semestr

    def set_semestr(self, semestr):
        if 1 <= semestr <= 8:
            self.__semestr = semestr
        else:
            self.__semestr = 1

    def get_predmet(self):
        return self.__predmet

    def set_predmet(self, predmet):
        if len(predmet) >= 3:
            self.__predmet = predmet
        else:
            self.__predmet = 3

    def get_attestaciya(self):
        return self.__attestaciya

    def set_attestaciya(self, attestaciya):
        self.__attestaciya = attestaciya
student1 =RPA("Иванов","Коля",7,"Математика","есть")
student2 =RPA("Иванов","Коля",4,"Русский Язык","есть")
print(student1.get_familiya())
print(student1.get_imya())
print(student1.get_semestr())
print(student1.get_predmet())
print(student1.get_attestaciya())
print('\n')
print(student2.get_familiya())
print(student2.get_imya())
print(student2.get_semestr())
print(student2.get_predmet())
print(student2.get_attestaciya())