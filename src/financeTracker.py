import csv
import os
from datetime import datetime
from transaction import Transaction

class Finances:
    expense_categories = ["Groceries", "Fuel", "Gifts", "Charity", "Household", "Rent", "Bills", "Misc"]
    income_categories = ["Salary", "Gifts", "Dividends", "Student Loans", "Side Hustles", "Misc"]

    def __init__(self):
        self.transactions = []
        return;

    def financeInterface(self):
        print("Welcome to the finance interface!")
        return;

    def recommendedBreakdown(self):
        print(f"Needs: {self.week_pay*0.5}\n")
        print(f"Wants: {self.week_pay*0.3}\n")
        print(f"Savings: {self.week_pay*0.2}\n")
        return

    def addIncome(self):
        print("Adding an income")

        category = Transaction.transaction_category(self, self.income_categories);
        date = Transaction.transaction_date(self);
        amount = Transaction.transaction_amount(self);
        desc = Transaction.transaction_desc(self);

        new_expense = Transaction(category, date, amount, desc, True)

        choice = str(input(f"{new_expense}\nConfirm this transaction? (Y/N)"))
        if choice.strip().upper() == "Y":
            self.transactions.append(new_expense);
            print("Added income successfully!\n")
        else:
            print("Transaction cancelled")
        return;

    def quickAddIncome(self, date, amount, desc, is_income = True, category = "Misc"):
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        try:
            new_income = Transaction(category, date_obj, amount, desc, True)
            self.addTransactionCSV(new_income)
            print(f"Income added")
        except ValueError:
            print("Invalid input");
        return;

    def quickAddExpense(self, date, amount, desc, is_income = False, category = "Misc"):
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        try:
            new_expense = Transaction(category, date_obj, amount, desc, False)
            self.addTransactionCSV(new_expense)
            print(f"Expense added")
        except ValueError:
            print("Invalid input");
            return;
    
    def addExpense(self):
        print("Adding an expense...\n")

        category = Transaction.transaction_category(self, self.expense_categories);
        date = Transaction.transaction_date(self);
        amount = Transaction.transaction_amount(self);
        desc = Transaction.transaction_desc(self);

        new_expense = Transaction(category, date, amount, desc, False)

        choice = str(input(f"{new_expense}\nConfirm this transaction? (Y/N)"))
        if choice.strip().upper() == "Y":
            self.transactions.append(new_expense);
            self.addTransactionCSV(new_expense)
            print("Added expense successfully!\n")
        else:
            print("Transaction cancelled")
        #add to csv file
        return;

    def getAllTransactions(self):
        for t in self.transactions:
            print(self.transactions[t])
        return;

    def addTransactionCSV(self, transaction, filename = "transactions.csv"):
        file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0
        with open(filename, mode = "a", newline = '', encoding = 'utf-8') as file:
            writer = csv.writer(file);
            if not file_exists:
                writer.writerow(["ID", "Type" ,"Amount", "Date", "Category", "Description"])
            
            transaction_type = "Income" if transaction.is_income else "Expense"
            writer.writerow([
                transaction.id, transaction_type, transaction.amount,
                transaction.date.strftime("%y-%m-%d"), transaction.category,
                transaction.desc])
        return;

    def loadTransactions(self, filename = "transactions.csv"):
        if not os.path.exists(filename):
            print("No such transaction file exists")
            return;
        with open(filename, mode = 'r', newline = '', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)

    def clearTransactions(self, filename = "transactions.csv"):
        with open(filename, mode = 'w', newline = '', encoding = 'utf-8') as file:
            file.write("")
        return;

"""to be implemented:
1. searching methods by each attribute of the transactions in the file
2. deleting transactions
3. editing transactions"""