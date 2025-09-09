# This interface will be turned graphical and updated along the way

class Account:
    def __init__(self,acc_owner,_balance):
        self.acc_owner = acc_owner
        self._balance = _balance

    def deposit(self,dep_amount):
        self._balance += dep_amount
        print(f"you've deposited {dep_amount} successfully and your account balance is now {self._balance}")

    def withdraw(self, with_amount):
        wanna_Cancel = False
        print(f"you're withdrawing the amount of {with_amount}")
        while with_amount > self._balance and wanna_Cancel == False:
            wanC = input('Invalid amount, do you want to cancel y or n? ')
            if wanC == 'y':
                wanna_Cancel = True
            else:
                with_amount = float(input(f'please enter an valid amount to withdraw <= {self._balance}: '))
        self._balance -= with_amount
        print(f"you've withdrawn successfully \nbalance {self._balance}")
    
    def get_balance(self):
        return f'your balance is currently: {self._balance}'
    
class SavingsAccount(Account):
    def __init__(self, acc_owner,_balance,interest_rate):
        super().__init__(acc_owner,_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        inter = self._balance * (self.interest_rate)
        super().deposit(inter)

John_Acc = SavingsAccount('John Doe', 500,0.05)
print(John_Acc.get_balance())
John_Acc.deposit(200)
John_Acc.withdraw(100)
John_Acc.withdraw(700)
John_Acc.add_interest()
print(John_Acc.get_balance())
