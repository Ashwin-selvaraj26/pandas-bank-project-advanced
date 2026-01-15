import pandas as pd

transactionDf = pd.read_csv('Transactions/arun.csv')

df = transactionDf[transactionDf['Transaction Type'] == 'Send']
print(df) 
df.loc[:,"Change in balance"] = df["Change in balance"].abs()
print(df) 
summary = df.groupby("Category")["Change in balance"].sum()
print(summary) 