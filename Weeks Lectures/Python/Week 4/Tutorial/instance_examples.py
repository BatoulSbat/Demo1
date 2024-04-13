#instance method
class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        """
        the deposit and withdraw methos are instance methods
        because they operate on a specific bank account instance.
        they have access to and can modify the instance  specific
        attributes i.e. balance
        """
        self.balance += amount
        print(f"Deposited £{amount}. New balance: £{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw £{amount}. New balance: £{self.balance}")
        else:
            print("Insifficient funds")

#create an instance
account = BankAccount(name = "Amare", balance = 1000)
account.deposite(200)
account.withdraw(500)

