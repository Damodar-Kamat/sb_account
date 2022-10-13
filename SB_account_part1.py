import datetime
class SB_Bank():
    def __init__(self):
        self.name = "ABC Bank"
        self.address = "RR nagar,Banglore"
        print("Welcome to",self.name)
        print(self.address)
class ABC_bank(SB_Bank):
    def __init__(self,amount1,open_date):
        self.passbook = {open_date:["Balance : "+str(amount1)]}
        self.c_name=input("enter the customer name :")
        self.acc_no =input("enter the Account number :")
        self.balance = amount1
    def c_details(self):
        print("the name of the customer is :",self.c_name)
        print("the account number of the customer is :",self.acc_no)
        print("Balance :",self.balance)
    def deposit(self,amount,date):
        self.balance += amount
        if(self.passbook.get(date)==None):
            self.passbook[date] = []
            self.passbook[date].append("Deposited "+str(amount)+" on "+date+"| Balance : " + str(self.balance))
            print("the deposited amount is :",amount," on ",date)
    def withdraw(self,amount,date):
        if(self.balance-amount<0):
            print("Not Enough balance in Account!")
            return
        self.balance -= amount
        print("the withdrew amount is :",amount," on ",date)
        if(self.passbook.get(date)==None):
            self.passbook[date] = []
            self.passbook[date].append("Withdrew "+str(amount)+" on "+date+"| Balance : " + str(self.balance))
        
    def print_passbook(self):
        sdate = input("\n Enter start Date : ")
        edate = input(" Enter end Date : ")
        print("the name of the customer is :",self.c_name)
        print("the account number of the customer is :",self.acc_no)
        if(sdate=="all" or sdate==""):
            for date in self.passbook:
                for entry in self.passbook[date]:
                    print(" ",date," :",entry)
        else:
            sdate_parsed = datetime.datetime.strptime(sdate,'%d/%M/%Y')
            edate_parsed = datetime.datetime.strptime(edate,'%d/%M/%Y')
            for entry_date in self.passbook:
                ent_parsed = datetime.datetime.strptime(entry_date,'%d/%M/%Y')
                if(ent_parsed>=sdate_parsed and ent_parsed<=edate_parsed):
                    for entry in self.passbook[entry_date]:
                        print(" ",entry_date," :",entry)
choice = 0
amount = 0
obj = ABC_bank(5000,'21/04/2022')
tdate = '23/04/2022'
while(choice!=4):
    print("1.customer details\n2.Deposit\n3.Withdraw\n4.Print passbook\n5.Exit")
    choice=int(input("enter your choice :"))
    if(choice==1):
        obj.c_details()
    if(choice==2):
        amount = int(input("\n Enter Amount to Deposit : "))
        obj.deposit(amount,tdate)
    if(choice==3):
        amount = int(input("\n Enter Amount to WithDraw : "))
        obj.withdraw(amount,tdate)
    if(choice==4):
        obj.print_passbook()