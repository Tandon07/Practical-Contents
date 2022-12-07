class Person1:
    def __init__(self,n,surname,emailid,year_of_birth):
        #                   In python __init__ is a constructor
        #                   self(self is not a reserved keyword, yahan kuchh bhi rakh sakte, jo bhi first variable rakhenge init me vo pointer ban jayega)
        #                   self is a kind of pointer pointing to a particular class
        self.name=n
        self.surname=surname
        self.emailid=emailid
        self.year_of_birth=year_of_birth

    def age(self,current):
        return current-self.year_of_birth


anuj_var=Person1("anuj","bhandari","anuj@gmail.com",1995)
#  anuj_var is a variable of class(Person)
print(anuj_var.name)
print(anuj_var.surname)
print(type(anuj_var))
print(anuj_var.age(2021))

