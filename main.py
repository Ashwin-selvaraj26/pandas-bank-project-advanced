import pandas as pd
import datetime as dt
import os

class BankAccount :
    def __init__(self,name,balance=0):
        self.name = name
        self.__balance = balance
        self.transactionDf = pd.DataFrame(columns=['Timestamp','Transaction Type','Change in balance'])
        
        if not os.path.exists('Transactions'):
            os.makedirs('Transactions')
            
        try:
            self.transactionDf = pd.read_csv(f'Transactions/{self.name}.csv')
            self.updateBalance()
        except FileNotFoundError:
            self.updateCsv()
            
    def viewBalance (self) :
        print(f"The current balance is : {self.__balance}")
        
    def viewTransactionHistory(self) :
        print(self.transactionDf)
        
    def updateBalance (self) :
        self.__balance = sum(self.transactionDf['Change in balance'])

    def processTransaction(self,inp) :
        now = dt.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        transactionType = ''
        
        amount = int(input("Enter the amount: "))
        
        if inp == 1 :
            transactionType = 'Deposit'
        else :
            if amount == 0:
                print("Can't withdraw 0")
                return
            if self.__balance < amount:
                print("Insufficient funds!")
                return
            transactionType = 'Withdrawal'
            amount = -(amount)
            
        self.transactionDf.loc[len(self.transactionDf)] = [now,transactionType,amount]
        self.updateBalance()
        self.updateCsv()

    def updateCsv (self) :
        self.transactionDf.to_csv(f'Transactions/{self.name}.csv', index=False)


       
def main():
    username = input("Enter your username : ")
    usernameAcc = BankAccount(username)
    while True:
        homeScreen()
        userInput = int(input("Enter input here : "))
        match userInput:
            case 1:
                usernameAcc.processTransaction(1)
            case 2:
                usernameAcc.processTransaction(2)
            case 3:
                usernameAcc.viewBalance()
                input("Go back : ")
            case 4:
                usernameAcc.viewTransactionHistory()
                input("Go back : ")
            case 5:
                return
            case _:
                print("Enter a valid input.")

def homeScreen():
    print("--- Your Bank ---")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.View Transaction history")
    print("5.Quit")
    print("-----------------")
    print("")


main()
