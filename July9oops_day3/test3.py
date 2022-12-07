class ineuron:
    def students(self):
        print("print the details of all the students")
    def achievers(self):
        print("print the list of all the achievers")
    def hallOfFame(self):
        print("print all the hall of fame")

class ineuron_vision(ineuron):
    def students(self):
        print("Hum hai ineuron vision wale students")

obj=ineuron_vision()
obj.students()            #This will print child class method  and this is called METHOD OVERRIDING

