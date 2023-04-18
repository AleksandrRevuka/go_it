from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(value for value in self.data if value > 0)
    
        
k = AmountPaymentList([1, -3, 4])
print(k.amount_payment())
        