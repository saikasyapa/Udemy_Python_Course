import datetime
import pytz

class Account:
    """ Simple account class with balance"""
    @staticmethod
    def _current_time():                               ### static method means in that we are not using self so it is applicable for all methods like previous example power_source
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f"Account created for {name}")

    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount, 'deposit'))
            self.transaction_list.append((Account._current_time(), amount, 'deposit'))
            self.show_transactions()
            self.show_balance()

    def withdraw(self, amount):
        if (amount > 0) and (amount <= self.balance):
            self.balance = self.balance - amount
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount, 'withdraw'))
            self.transaction_list.append((Account._current_time(), amount, 'withdraw'))
            self.show_transactions()
            self.show_balance()

        elif amount <=0:
            print("Invalid amount, Please check the entered amount")

        else:
            print("Insufficient balance")
            self.show_balance()

    def show_balance(self):
        print(f"balance is {self.balance}")

    def show_transactions(self):
        for date, amount,trans_type in self.transaction_list:
            if trans_type == 'deposit':
                print(f"Money deposited in {date.astimezone()} and the amount is {amount} ")
            elif trans_type == 'withdraw':
                print(f"Money withdraw in {date.astimezone()} and the amount is {amount} ")



if __name__ == '__main__':
    user1 = Account('sai',15000)
    user1.deposit(5000)
    user1.withdraw(2000)




