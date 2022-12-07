# from test2 import employee
from utils.util import Person2


class Person:
    def __init__(self,name,surname,yob):
        self._name=name                     #'_' before var_name means protected
        self.__surname=surname                #'__' before var_name means private
        self.yob=yob

sudh=Person("Sudhanshu","Kumar",1998)
obj4= Person2("dhb","iauehdiu",1999)
print(sudh._name)
print((sudh._Person__surname))
print(sudh.yob)
print(obj4._name)




