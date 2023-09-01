class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
        
    def withdraw(self,amount):
        if amount > 0:
            self.balance -= amount
            return True
        else:
            return False
    def get_balance(self):
        print(f"Ваш баланс: {self.balance}")

account = BankAccount(0)

command = ["deposit", "withdraw", "balance", "quit",]

while True:
    cmd = input("Введите команду:")
    if cmd == "deposit":
        amount = float(input("Введите сумму пополнения баланса: "))
        account.deposit(amount)
    if cmd == "withdraw":
        amount = float(input("Введите сумму снятия средств с баланса: "))
        account.withdraw(amount)
    if cmd == "balance":
        account.get_balance()
    if cmd == "quit":
        break
    if not cmd in command:
        print("Error Command!")

            
