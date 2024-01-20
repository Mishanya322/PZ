class Student:
 def __init__(self, name, age, group, evl):
    self.name = name
    self.age = age
    self.group = group
    self.evl = evl
 def cal_evl(self):
     return sum(self.evl)/len(self.evl) if len(self.evl) !=0 else 0
tom= Student("Tom",2,"IS(PRO)-11",[3,4,5,4,5,3,4,5,5])
evl_z=tom.cal_evl()
print(f"Средняя оценка студента{tom.name} равна {evl_z}")