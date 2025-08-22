import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as py

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
def incomeByDates(fin):
    #plot a histogram of income by month
    #create a dataset with dates and amounts, filtered by is_income
    #dataset is taken from fin(getAllTransactions), returns fin.transactions
    full_dataset = fin.getAllTransactions()
    filtered_records = pd.DataFrame(trans.__dict__ for trans in full_dataset if trans.is_income)[["date", "amount"]]
    filtered_records["month_name"] = filtered_records["date"].dt.strftime("%m")
    #group by month and sum amounts
    monthly_sums = filtered_records.groupby("month_name")["amount"].sum()
    #sort by calendar order

    return filtered_records
def expensesByDates(fin):
    return
def netIncomeByDates(fin):
    return
def mostCommonCategories(fin):
    return