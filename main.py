import pandas as pd
import datetime as dt
import os
import matplotlib.pyplot as plt


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
        self.transactionDf = pd.DataFrame(
            columns=["Timestamp", "Transaction Type", "Category", "Change in balance"]
        )

        if not os.path.exists("Transactions"):
            os.makedirs("Transactions")

        try:
            self.transactionDf = pd.read_csv(f"Transactions/{self.name}.csv")
            self.updateBalance()
        except FileNotFoundError:
            self.updateCsv()

    def viewBalance(self):
        print(f"The current balance is : {self.__balance}")

    def viewTransactionHistory(self):
        print(self.transactionDf)

    def updateBalance(self):
        self.__balance = sum(self.transactionDf["Change in balance"])

    def processTransaction(self, inp):
        now = dt.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        transactionType = ""

        amount = int(input("Enter the amount: "))
        category = '-'
        
        if inp == 1:
            transactionType = "Recive"
        else:
            if amount == 0:
                print("Can't Send 0")
                return
            if self.__balance < amount:
                print("Insufficient funds!")
                return
            while True :
                catList = ['food','service','rent','product']
                category = input("Enter the category (Food/Rent/Product/Service) : ")
                
                if (category.lower() in catList):
                    break
                else :
                    print("Invalid input!")
                
                
            transactionType = "Send"
            amount = -(amount)

        self.transactionDf.loc[len(self.transactionDf)] = [now, transactionType, category, amount]
        self.updateBalance()
        self.updateCsv()

    def updateCsv(self):
        self.transactionDf.to_csv(f"Transactions/{self.name}.csv", index=False)
        
    def expenseAnalytics (self) :
        df = self.transactionDf[self.transactionDf['Transaction Type'] == 'Send']
        df.loc[:,"Change in balance"] = df["Change in balance"].abs()
        summary = df.groupby("Category")["Change in balance"].sum()
        summary.plot(kind='barh')
        plt.title("Expense analytics")
        plt.xlabel("Amount spent")
        plt.ylabel("Category")
        plt.tight_layout()
        plt.show()


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
                input("Press any button to go back : ")
            case 4:
                usernameAcc.viewTransactionHistory()
                usernameAcc.expenseAnalytics()
                input("Press any button to go back : ")
            case 5:
                return
            case _:
                print("Enter a valid input.")


def homeScreen():
    print("--- Your Account ---")
    print("1.Recive")
    print("2.Send")
    print("3.Check balance")
    print("4.View Transaction history")
    print("5.Quit")
    print("-----------------")
    print("")


main()
