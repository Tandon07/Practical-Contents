

class Person:

    def age(self,current_yr,year_of_birth):
        return current_yr-year_of_birth

    def emailId(self,email_id):
        print("take mail id from person and print it",email_id)

    def askname(self):
        name=input("enter your name")
        return name

sudh =Person()
anuj=Person()
garg=Person()
sudh.emailId("skj@Vgmail.com")
print(anuj.askname())
print(garg.age(2022,1998))
