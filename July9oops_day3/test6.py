class ineuron:
    def students (self) :
        print("print a students details")
class class_type:
    def students (self) :
        print ("print the class type of students")


def ineuron_external(a):       #This one single function is able to handle i and j both
    a.students()
                               # This function is behaving like a brigde or connection b/w all the classes

                               #This concept is called *********      POLYMORPHISM             ****************


i =ineuron()
j = class_type ()
ineuron_external (i)
ineuron_external (j)



# def test(a,b):
#     return a+b
#
# print(test(3,4))
# print(test("saurabh","tandon"))
