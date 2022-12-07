class car:
    def __init__(self,body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre
    def milage(self):
        print("milage of this car")

class tata(car):
    pass

t=tata("solid","v6","super grippy")
print(t.body)
c=car("semiSolid","v5","MRF")
print(t.tyre)
print(c.tyre)
