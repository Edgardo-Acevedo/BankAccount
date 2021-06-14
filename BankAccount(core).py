class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        if(self.balance > 0):
            print(f'su saldo es {self.balance}')
        if(self.balance < 0):
            print(f'su saldo {self.balance} es insuficiente')
        return self
    
    def yield_interest(self):
        if(self.balance > 0):
            print(f'el saldo aumentado es {self.balance + (self.balance*self.int_rate)} \n')
        return self
    
# CUENTA_BANCARIA_UNO
Cuenta_Bancaria_Uno = BankAccount(0.03, 100)
Cuenta_Bancaria_Uno.deposit(10).deposit(15).deposit(20).withdraw(70).display_account_info().yield_interest()

# CUENTA_BANCARIA_DOS
Cuenta_Bancaria_Dos = BankAccount(0.02, 150)
Cuenta_Bancaria_Dos.deposit(20).deposit(25).withdraw(10).withdraw(15).withdraw(20).withdraw(25).display_account_info().yield_interest()

    
