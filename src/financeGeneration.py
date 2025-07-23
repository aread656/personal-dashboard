from datetime import datetime, timedelta
import pandas as pd
import random
from transaction import Transaction

income_categories = ["Pay", "Gift", "Dividend", "Loans", "Misc"]
expense_categories = ["Bills", "Fuel", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Misc"]

def random_dates(start, end):
    delta = end - start
    return (start + timedelta(days = random.randint(0, delta.days))).strftime("%Y-%m-%d")

def generate_student_income(n = 50):
    transactions = []
    start_date = datetime.now() - timedelta(days = 365)
    end_date = datetime.now()

    for i in range(n):
        category = random.choices(
            population = income_categories,
            weights = [50, 20, 8, 2, 20],
            k = 1
        )[0]

        match category:
            case "Pay":
                amount = round(random.uniform(80, 300), 2)
                description = "Part-time job"
            case "Gift":
                amount = round(random.uniform(20, 40), 2)
                description = "Gifts from family/friends"
            case "Dividend":
                amount = round(random.uniform(0.1, 5), 2)
                description = "Stock dividends"
            case "Loans":
                amount = round(random.uniform(1200, 2000), 2)
                description = "Student Loans"
            case "Misc":
                amount = round(random.uniform(2, 20), 2)
                description = "Miscellaneous"
        
        date = random_dates(start_date, end_date)

        new_trans = Transaction(
            category = category,
            date = date,
            amount = amount,
            desc = description,
            is_income = True
        )
        transactions.append(new_trans)

    return transactions
    
def generate_student_expenses(n = 150):
    transactions = []
    start = datetime.now() - timedelta(days = 365)
    end = datetime.now()

    for i in range(n):
        category = random.choices(
            population = expense_categories,
            weights = [5, 10, 30, 5, 10, 2, 15, 20],
            k = 1
        )[0]

        match category:
            case "Bills":
                amount = round(random.uniform(420, 450), 2)
                description = "Monthly rent and bills"
            case "Fuel":
                amount = round(random.uniform(30, 70), 2)
                description = "Car fuel"
            case "Groceries":
                amount = round(random.uniform(15, 40), 2)
                description = "Groceries"
            case "Clothing":
                amount = round(random.uniform(15, 40), 2)
                description = "Clothing"
            case "Charity":
                amount = round(random.uniform(15, 30), 2)
                description = "Foodbank/charity donation"
            case "Emergency":
                amount = round(random.uniform(75, 300), 2)
                description = "Emergency repairs/purchases"
            case "Leisure":
                amount = round(random.uniform(10, 25), 2)
                description = "Entertainment and Leisure"
            case "Misc":
                amount = round(random.uniform(5, 20), 2)
                description = "Other miscellaneous"

        date = random_dates(start, end)

        new_trans = Transaction(
            category = category,
            date = date,
            amount = amount,
            desc = description,
            is_income = False
        )
        transactions.append(new_trans)
    
    return transactions

#to do: generate method to translate actual bank statement csv
#read the file
def CSVStatementConverter(self):
    return
#modify the file to give correct categories
#assign each provided variable to the chosen variables in the other code
#write and save the file as a new file