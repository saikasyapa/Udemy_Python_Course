import datetime
import pytz

class Account:
    """ Simple account class with balance"""
    @staticmethod
    def _current_time():                               ### static method means in that we are not using self so it is applicable for all methods like previous example power_source
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,name, balance):
        self._name = name
        self.__balance = balance                  ### attributes whose name is start with single _ are for internal use only
        self._transaction_list = []
        # self.transaction_list = [(Account._current_time(),balance, '')]
        print(f"Account created for {name}")
        # self.show_balance()


    def deposit(self,amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount, 'deposit'))
            self._transaction_list.append((Account._current_time(), amount, 'deposit'))
            self.show_balance()



    def withdraw(self, amount):
        if (amount > 0) and (amount <= self.__balance):
            self.__balance = self.__balance - amount
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount, 'withdraw'))
            self._transaction_list.append((Account._current_time(), amount, 'withdraw'))
            self.show_balance()



        elif amount <=0:
            print("Invalid amount, Please check the entered amount")

        else:
            print("Insufficient balance")
            self.show_balance()

    def show_balance(self):
        print(f"balance is {self.__balance}")

    def show_transactions(self):
        for date, amount,trans_type in self._transaction_list:
            if trans_type == 'deposit':
                print(f"Money deposited in {date.astimezone()} and the amount is {amount} ")
            else:
                if trans_type == 'withdraw':
                    print(f"Money withdraw in {date.astimezone()} and the amount is {amount} ")



if __name__ == '__main__':
    user1 = Account('sai',0)
    user1.deposit(5000)
    user1.withdraw(100)
    user1.show_transactions()
    print('*' * 40)
    user2 = Account('curry',200)
    user2.__balance=10000
    user2.show_balance()
    print("After deposit 800")
    user2.deposit(800)
    print("After withdraw 350")
    user2.withdraw(350)
    print("All Transactions")
    user2.show_transactions()
    print(user2.__dict__)
    ### to mess or change that
    user2._Account__balance = 40
    user2.show_balance()





