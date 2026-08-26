from datetime import datetime
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from .finance import Finance

def transactions_into_dataframe(fin: Finance) -> pd.DataFrame:
    transactions = fin.getAllTransactions()
    if not transactions:
        return pd.DataFrame(columns=["date","amount","category","type"])
    df = pd.DataFrame([
        {"date":trans.date,
        "amount":trans.amount,
        "category":trans.category,
        "type":trans.type}
        for trans in transactions
    ])
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.strftime("%b")
    return df

#----------------------------------------------------------
#               Record Listing & Filtering                 
#----------------------------------------------------------
def all_incomes_or_expenses(fin,is_income:bool):
    return [t for t in fin.getAllTransactions() if t.type == is_income]

def filter_records_by_dates(fin:Finance,start:datetime,end:datetime,printing=False):
    filtered_records = [
        t for t in fin.getAllTransactions()
        if start <= datetime.strptime(t.date,"%Y-%m-%d") <= end
    ]
    if printing:
        for t in filtered_records: print(t)
    return filtered_records

#-------------------------------------------------
#                Totals & Net Income            
#--------------------------------------------------
def total_income(fin:Finance):
    return sum(t.amount for t in fin.getAllTransactions() if t.type == True)

def total_expenses(fin:Finance):
    return sum(t.amount for t in fin.getAllTransactions() if t.type == False)

def netIncome(fin):
    return total_income(fin) - total_expenses(fin)

#----------------------------------------------------
#                   Charts & Graphs                 
#----------------------------------------------------
def monthly_bar_chart(df:pd.DataFrame, y_col, title):
    plt.figure(figsize=(8,5))
    plt.title(title)
    sns.barplot(data=df,x="month_name",y=y_col)
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()

def income_by_dates(fin):
    df = transactions_into_dataframe(fin)
    income_records = df[df["type"]==True]
    monthly = income_records.groupby(["month_name","month"])["amount"].sum().reset_index()
    monthly_bar_chart(monthly,"amount","Income by month")

def expenses_by_dates(fin):
    df = transactions_into_dataframe(fin)
    expense_records = df[df["type"]==False]
    monthly = expense_records.groupby(["month_name","month"])["amount"].sum().reset_index()
    monthly_bar_chart(monthly,"amount","Expenses by month")

def net_income_by_dates(fin):
    df = transactions_into_dataframe(fin)

    income_records = df[df["type"]==True].groupby(["month_name","month"])["amount"].sum().reset_index()
    expense_records = df[df["type"]==False].groupby(["month_name","month"])["amount"].sum().reset_index()
    net_income = pd.merge(left=income_records,right=expense_records,how="outer",on=["month_name","month"]).fillna(0)
    #net_income now a merged dataframe of both previous frames joined together
    net_income["net"] = net_income["amount_x"] - net_income["amount_y"]
    net_income = net_income.sort_values("month")

    monthly_bar_chart(net_income,"net","Net income by month")

def most_common_categories(fin):
    df = transactions_into_dataframe(fin)
    category_counts = df["category"].value_counts().reset_index()
    category_counts.columns = ["category","count"]

    plt.figure(figsize=(8,5))
    plt.title("Most common categories")
    sns.barplot(category_counts,x="category",y="count")
    plt.xlabel("Category")
    plt.ylabel("Frequency")
    plt.show()

def amount_by_category(fin):
    df = transactions_into_dataframe(fin)

    category_sums = df.groupby("category")["amount"].sum().reset_index()

    plt.figure(figsize=(8,5))
    plt.title("Amounts by category")
    sns.barplot(category_sums,x="category",y="amount")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()