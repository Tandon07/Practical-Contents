# MULTILEVEL INHERITENCE


class bank:
    def transaction(self):
        print("total transaction")
    def account_opening(self):
        print("This will show your bank account status")
    def deposit(self):
        print("This will  show your deposited amount")
class HDFC(bank):
    def hdfcToIcici(self):
        print("This will show transaction of HDFC to ICICI")

class ICICI(HDFC):
    pass

i=ICICI()
i.transaction()
i.hdfcToIcici()




