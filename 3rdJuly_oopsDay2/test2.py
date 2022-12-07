import test1
print(test1)
obj3=test1.Person("dcb","shgfh",1987)
print(obj3.yob)
print(obj3._name)
print(obj3._Person__surname)

class person:
    _name="sudh"
    __surname="Kumar"
    yob=1990


    def _age(self,current_yr):
        return current_yr-self.yob
    def __age1(self,current_yr):
        return current_yr-self.yob



obj=person()
print(obj)
print(obj._age(2000))
print(obj._person__age1(2020))




class employee(person): #Inheritance: employee is inheriting person
    _name = "Ravi"
    __surname = "singh"
    yob = 2000

obj1=employee()

print(obj1.yob)
print(obj1._person__surname)
print(obj1._employee__surname)
print(obj1._name)
print(obj1._name)
print(obj1._age(2022))
print(obj1._person__age1 (2022))




