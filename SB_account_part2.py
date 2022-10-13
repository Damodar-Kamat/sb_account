import datetime
class SB_acc:
    def __init__(self):
        self.name='ABC Bank'
        self.address='RR nagar,Bangalore'
        print("Welcome to",self.name)
        print(self.address)
        
class atm(SB_acc):
    def __init__(self,atm_name,atm_balance,open_date):
        self.transactions = {open_date:[" Balance : "+str(atm_balance)]}
        self.name = atm_name
        self.balance = atm_balance
    def add_cash(self,date):
        amount = int(input("Enter Amount to Deposit : "))
        self.balance += amount
        print("the amount deposited is :",amount," on ",date)
        if(self.transactions.get(date)==None):
            self.transactions[date] = []
            self.transactions[date].append(" Bank credited "+str(amount)+" on "+date+"| Balance : " + str(self.balance))
    def check_balance_threshold(self,date):
        if(self.balance<=5000):
            self.add_cash(10000,date)
    def deposit(self,user,amount,date):
        self.balance += amount
        if(self.transactions.get(date)==None):
            self.transactions[date] = []
            self.transactions[date].append(" "+user+" credited "+str(amount)+" on "+date+"| Balance : " + str(self.balance))
    def withdraw(self,user,amount,date):
        if(self.balance-amount<0):
            raise ValueError("Not Enough balance in AMT!")
            return
        self.balance -= amount
        if(self.transactions.get(date)==None):
            self.transactions[date] = []
            self.transactions[date].append(" "+user+" debited "+str(amount)+" on "+date+"| Balance : " + str(self.balance))
            self.check_balance_threshold(date)
    def print_transactions(self):
        sdate = input("\n Enter start Date : ")
        edate = input(" Enter end Date : ")
        if(sdate=="all" or sdate==""):
            for date in self.transactions:
                for entry in self.transactions[date]:
                    print(" ",date," :",entry)
        else:
            sdate_parsed = datetime.datetime.strptime(sdate,'%d/%M/%Y')
            edate_parsed = datetime.datetime.strptime(edate,'%d/%M/%Y')
            for entry_date in self.transactions:
                ent_parsed = datetime.datetime.strptime(entry_date,'%d/%M/%Y')
                if(ent_parsed>=sdate_parsed and ent_parsed<=edate_parsed):
                    for entry in self.transactions[entry_date]:
                        print(" ",entry_date," :",entry)
atms = []
choice=0
date = "21/04/2022"
                        
for i in range(0,3):
    atms.append(atm("ABC ATM"+str(i+1),10000,date))
atms[0].withdraw("damodar",1500,"21/04/2022")
atms[0].withdraw("rohan",5500,"21/04/2022")
while(choice!=4):
    print("1.atm status\n2.transactions\n3.Deposit\n4.exit\n")
    choice=int(input("enter your choice :"))
    if(choice==1):
        print(" ","Name"," ","Balance"," ","transactions")
        for atm in atms:
            print(" ",atm.name," ",atm.balance," \t",len(atm.transactions))
    if(choice==2):
        atm_id = int(input("\n Enter pin : "))
        atms[atm_id].print_transactions()
    if(choice==3):
        atm_id = int(input("\n Enter pin : "))
        atms[atm_id].add_cash(date)
