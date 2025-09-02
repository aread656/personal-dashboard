import numpy as np
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

def totalIncome(fin) -> float:
    return sum(t.amount for t in fin.getAllTransactions() if t.is_income and t.amount < 1000)
def totalExpenses(fin) -> float:
    return sum(t.amount for t in fin.getAllTransactions() if not t.is_income and t.amount < 1000)
def netIncome(fin) -> float:
    return totalIncome(fin) - totalExpenses(fin)

def datesDataset(fin, income_true_false):
    full_dataset = fin.getAllTransactions()
    filtered_dataset = pd.DataFrame(
        {"date": trans.date,
         "amount": trans.amount}
        for trans in full_dataset if trans.is_income == income_true_false)
    filtered_dataset["month"] = filtered_dataset["date"].dt.month
    filtered_dataset["month_name"] = filtered_dataset["date"].dt.strftime("%m")
    return filtered_dataset
def plotIncomeOrExpensesByDates(fin, monthly_sums):
    sns.barplot(data = monthly_sums, x = "month_name", y = "amount",
                order = monthly_sums["month_name"])
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()
    return
def incomeByDates(fin):
    income_dates_dataset = datesDataset(fin, True)
    monthly_sums = income_dates_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    plt.title("Income by month")
    plotIncomeOrExpensesByDates(fin, monthly_sums)
    return
def expensesByDates(fin):
    expenses_dates_dataset = datesDataset(fin, False)
    monthly_sums = expenses_dates_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    plt.title("Expenses by month")
    plotIncomeOrExpensesByDates(fin, monthly_sums)
    return
def netIncomeByDates(fin):
    income_dataset = datesDataset(fin, True)
    expenses_dataset = datesDataset(fin, False)
    #create a net dataset from each dataset's sums
    income_sums = income_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    expenses_sums = expenses_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    net_sums = pd.merge(income_sums, expenses_sums, on = ["month", "month_name"], how = "outer")
    net_sums["net"] = net_sums["amount_x"] - net_sums["amount_y"]
    print(net_sums["net"])
    return

def mostCommonCategories(fin):
    return