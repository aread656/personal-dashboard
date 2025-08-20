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
    for i in range(12):
        break
    return
def expensesByDates(fin):
    return
def netIncomeByDates(fin):
    return
def mostCommonCategories(fin):
    return