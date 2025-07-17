from datetime import datetime, timedelta
import random

income_categories = ["Pay", "Gift", "Dividend", "Loans", "Misc"]
expense_categories = ["Bills", "Fuel", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Misc"]

def random_dates(start, end):
    delta = end - start
    return (start + timedelta(days = random.randint(0, delta.days))).strftime("%Y-%m-%d")

def generate_student_income(n = 50):
    transactions = []
    start_date = datetime.now - timedelta(days = 365)
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

        transactions.append({
            "date": date,
            "desctiption": description,
            "category": category,
            "amount": amount,
            "type": "expense"
        })

        return transactions

"""def loadSampleData(financeTracker):
    financeTracker.quickAddIncome("2025-07-03", 200, "Month's Salary", "Pay")
    financeTracker.quickAddExpense("2025-07-04", 50, "Electric Bill", "Bills")
    financeTracker.quickAddExpense("2025-07-05", 20, "Bowling", "Leisure")
"""
