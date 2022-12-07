# class ineuron:
#     def __init__(self):
#         # self.students="data science"        this will create a conflict of name variable and func name.
#     # This will show error as:  TypeError: 'str' object is not callable        so solution is to keep different names
#         self.students1 = "data science"
#     def students(self):
#         print(self.students1)
# i=ineuron()
# i.students()
# i.students1="data analytics"
# i.students()       #this will print data analytics this is called method overriding
#


class ineuron:
    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)
    def student_change(self,s):
        self.__students1=s

i=ineuron()
i.students()
# i.__students1="big data"        #Here it won't change the value, so it's solution is to create one more method student_change
i.student_change("big data by me")
i.students()


# if we have a private variable so with the help of objects we won't be able to reassign the variable values,
#     by calling a setter method from a class can be used to change the values so "student_change" is a setter method
# so any private variabe is not possible to modify directly for it a class method is reqd, via class method it can be modified



# This phenomenon is called  ********** ENCAPSULATION  ********************

# where you are not allowing user to modify directly but you can modify using setter method(class function)


# access=abstraction

# modification=encapsulation
