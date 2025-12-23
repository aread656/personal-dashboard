from datetime import datetime
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

"""statistics to be made:
    net income
    most common categories
    average income on a weekly/monthly basis"""

def allIncomesOrExpenses(fin, is_income: bool):
    return [trans for trans in fin.getAllTransactions() if trans.is_income == is_income]
def printAllIncomesOrExpenses(fin, is_income: bool):
    transactions = allIncomesOrExpenses(fin, is_income)
    for trans in transactions:
        print(str(trans))

def filterRecordsByDates(fin, start:datetime, end:datetime):
    filtered_records = pd.DataFrame(
        {"id":t.id,"type":t.is_income,"date":t.date,"category":t.category,
         "amount":t.amount,"desc":t.desc}
    for t in fin.transactions)
    mask = (filtered_records["date"] >= start) & (filtered_records["date"] <= end)
    return filtered_records.loc[mask]

def totalIncome(fin) -> float:
    return sum(t.amount for t in fin.getAllTransactions() if t.is_income and t.amount < 1000)
def totalExpenses(fin) -> float:
    return sum(t.amount for t in fin.getAllTransactions() if not t.is_income and t.amount < 1000)
def netIncome(fin) -> float:
    return totalIncome(fin) - totalExpenses(fin)

def datesDataset(fin, income_true_false: bool):
    filtered_dataset = pd.DataFrame(
        {"date": trans.date,
         "amount": trans.amount}
        for trans in fin.getAllTransactions() if trans.is_income == income_true_false)
    filtered_dataset["month"] = filtered_dataset["date"].dt.month
    filtered_dataset["month_name"] = filtered_dataset["date"].dt.strftime("%m")
    return filtered_dataset
def plotIncomeOrExpensesByDates(monthly_sums):
    sns.barplot(data = monthly_sums, x = "month_name", y = "amount",
                order = monthly_sums["month_name"])
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()
def incomeByDates(fin):
    income_dates_dataset = datesDataset(fin, True)
    monthly_sums = income_dates_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    plt.title("Income by month")
    plotIncomeOrExpensesByDates(monthly_sums)
def expensesByDates(fin):
    expenses_dates_dataset = datesDataset(fin, False)
    monthly_sums = expenses_dates_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    plt.title("Expenses by month")
    plotIncomeOrExpensesByDates(monthly_sums)
def netIncomeByDates(fin):
    income_dataset = datesDataset(fin, True)
    expenses_dataset = datesDataset(fin, False)
    #create a net dataset from each dataset's sums
    income_sums = income_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    expenses_sums = expenses_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    net_sums = pd.merge(income_sums, expenses_sums, on = ["month", "month_name"], how = "outer")
    net_sums["net"] = net_sums["amount_x"] - net_sums["amount_y"]
    plt.title("Net income by month")
    sns.barplot(data = net_sums, x = "month_name", y = "net")
    plt.xlabel("month")
    plt.ylabel("net amount")
    plt.show()

def mostCommonCategories(fin):
    dataset = fin.getAllTransactions()
    #create a count of transaction categories
    filtered_dataset = pd.DataFrame(
        {"category": trans.category} for trans in dataset)
    category_counts = filtered_dataset["category"].value_counts().reset_index()
    plt.figure(figsize = (8, 5))
    plt.title("Most common categories")
    sns.barplot(data = category_counts, x = "category", y = "count")
    plt.xlabel("Category")
    plt.ylabel("Number of occurrences")
    plt.show()
def amountsByCategory(fin):
    dataset = fin.getAllTransactions()
    filtered_dataset = pd.DataFrame(
        {"category": trans.category,
         "amount": trans.amount}
         for trans in dataset)
    category_sums = filtered_dataset.groupby(["category"])["amount"].sum().reset_index()
    plt.figure(figsize = (8, 5))
    plt.title("Amounts by category")
    sns.barplot(data = category_sums, x = "category", y = "amount")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()