class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        #                   In python __init__ is a constructor
        #                   self(self is not a reserved keyword, yahan kuchh bhi rakh sakte, jo bhi first variable rakhenge init me vo pointer ban jayega)
        #                   self is a kind of pointer pointing to a particular class
        self.name=name
        self.surname=surname

    # def age(self,current_yr,year_of_birth):
    #     return current_yr-year_of_birth
    # def age(self,current):
    #     return current-self.year_of_birth

    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

anuj_var=Person("anuj","bhandari","kahd@gmail.com",1998)
                                   #  nahi lega qki naya wala init humesha call hota h
#  anuj_var is a variable of class(Person)
print(anuj_var.name)
print(anuj_var.surname)
print(type(anuj_var))
# print(anuj_var.age(2021))

suraj_var=Person("suraj","bhandari")
print(suraj_var.surname)