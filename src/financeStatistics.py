import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

"""statistics to be made:
    net income
    most common categories
    average income on a weekly/monthly basis"""

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
    return filtered_dataset
def incomeByDates(fin):
    income_dates_dataset = datesDataset(fin, True)
    income_dates_dataset["month"] = income_dates_dataset["date"].dt.month
    income_dates_dataset["month_name"] = income_dates_dataset["date"].dt.strftime("%m")
    monthly_sums = income_dates_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")

    sns.barplot(data = monthly_sums, x = "month_name", y = "amount",
                order = monthly_sums["month_name"])
    plt.title("Income by Month")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()
    return
def expensesByDates(fin):
    expenses_dates_dataset = datesDataset(fin, False)
    expenses_dates_dataset["month"] = expenses_dates_dataset["date"].dt.month
    expenses_dates_dataset["month_name"] = expenses_dates_dataset["date"].dt.strftime("%m")
    monthly_sums = expenses_dates_dataset.groupby(["month", "month_name"])["amount"].sum().reset_index().sort_values("month")
    print(monthly_sums)

    sns.barplot(data = monthly_sums, x = "month_name", y = "amount")
    plt.title("Expenses by month")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()
    return
def netIncomeByDates(fin):
    income_dataset = datesDataset(fin, True)
    expenses_dataset = datesDataset(fin, False)
    #create a net dataset from each dataset's sums
    return


def mostCommonCategories(fin):
    return