balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount, "New Balance:", balance)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrawn:", amount, "New Balance:", balance)

def check_balance():
    print("Current Balance:", balance)

deposit(500)
withdraw(300)
withdraw(1500)
check_balance()

'''output-
Deposited: 500 New Balance: 1500
Withdrawn: 300 New Balance: 1200
Insufficient funds!
Current Balance: 1200
'''
