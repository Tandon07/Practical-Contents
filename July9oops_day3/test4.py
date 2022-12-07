class ineuron:
    __students ="data Science"

    def students(self):
        print("print te class of students",ineuron.__students)

i=ineuron()
i.students()
# i.__students       # I am not able to access directly the students variable, this is Abstraction
# Definition:-if we are trying to hide the real implementation, i is obj, i is trying to use student variable, if we are not giving
#     a direct access of an implementation to end user that is called as abstraction (data abstraction)

print(i._ineuron__students)




