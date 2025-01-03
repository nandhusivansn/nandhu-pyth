class account:
    def __init__(self,name,acc_no,acc_type,balance):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"you deposited RS{amount} successfully")
    def withdraw(self,amount):
        if(amount>self.balance):
            print("balance won't suffice")
            return
        else:
            self.balance-=amount
            print(f"withdraw RS{amount} successfully")
    def  display(self):
        print(f"name:{self.name}\t account no:{self.acc_no}\t account type:{self.acc_type}\t balance:{self.balance}")
acc_no=int(input("enter the account number"))
name=input("enter your name")
acc_type=input("enter account type")
ac1=account(name,acc_no,acc_type,0)
while(True):
    ac1.display()
    transaction=int(input("press 1 to deposit press 2 to withdraw"))
    if(transaction==1):
        ac1.deposit(int(input("enter the amount you want to deposit")))
    elif(transaction==2):
        ac1.withdraw(int(input("enter the amount you want to withdraw")))
    
    
