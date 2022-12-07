class Person2:
    def __init__(self,name,surname,yob):
        self._name=name                     #'_' before var_name means protected
        self.__surname=surname                #'__' before var_name means private
        self.yob=yob

sudh=Person2("Sudhanshu","Kumar",1998)
print(sudh._name)
print((sudh._Person2__surname))
print(sudh.yob)
