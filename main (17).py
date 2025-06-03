class atmsystem:
    def __init(self,initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self):
        amount=int(input("enter the money you want"))
        self.balance += amount
        print(f"{amount} desposited sucessful")
    def withdraw(self):
        amount=int(input("enter the money you want to withdraw"))
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdraw sucessfully")
    def check_balance(self):
        print(f"current balance:{self balance}")
            
    def exit(self):
        print("thanks for using our atm")

tm = atmsystem(initial_balance=35000)

while true:
    print("\n------atm menu------")
    print("1.deposit")
    print("2.withdraw")
    print("3.check balance")
    print("exit")
    choice = int(input("enter your choice:"))
    if choice ==1:
        atm.deposit()
    elif choice ==2:
        atm.withdraw()
    elif choice==3:
        atm.check_balance
    elif choice==4:
        atm.exit()
        break
    else:
        print("invalid choice please try again.")