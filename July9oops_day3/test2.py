# MULTIPLE INHERITENCE


class bank:
    def transaction(self):
        print("total transaction")
    def account_opening(self):
        print("This will show your bank account status")
    def deposit(self):
        print("This will  show your deposited amount")
    def test(self):
        print("This is a test method from bank")
class HDFC:
    def hdfcToIcici(self):
        print("This will show transaction of HDFC to ICICI")
    def test(self):
        print("This is a test method from HDFC")

class ineuronBank:
    def account_detail_icici(self):
        print("Print a account status in icici")


# class ICICI(bank,HDFC):
class ICICI(HDFC,bank,ineuronBank):
    pass

i=ICICI()
i.transaction()
i.hdfcToIcici()
i.test()  #IMPORTANT that it is calling that fucntion whose argument is first in child class
i.account_detail_icici()