class BankAccount :
    def __init__(self, balance):
        self.__balance = balance #private   

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.deposit(200)
print(account.__balance)
print("your balance is: ",account.get_balance())