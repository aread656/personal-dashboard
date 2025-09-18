import csv
import os
from datetime import datetime
from transaction import Transaction

class Finances:
    #a class which will manage a collection of transactions
    #the class will allow for adding, editing, and removing csv file records

    #a list of all income and expense categories:
    income_categories = ["Pay", "Gift", "Dividend", "Loans", "Misc"]
    expense_categories = ["Bills", "Fuel", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Misc"]

    def __init__(self, filename = "financeRecords.csv"):
        #initialise a finance class instance
        self.filename = filename
        self.balance = 0 
        self.transactions = []
        self.loadTransactions()

    #-------------Getters for Finances() instance-----------------#
    def getAllTransactions(self):
        return self.transactions
    
    #-------------Adding Income/Expenses with CLI----------------#
    def create_transaction(self, categories, is_income):
        #prompt the user to input transaction details
        category = Transaction.transaction_category(self, categories) 
        date = Transaction.transaction_date(self)
        amount = Transaction.transaction_amount(self)
        desc = Transaction.transaction_desc(self) 
        
        new_trans = Transaction(category, date, amount, desc, is_income)
        #check user if the transaction details are correct
        print("Please check the details of your transaction...\n")
        try:
            print(f"{new_trans}")
            confirm = input("Confirm transaction details? (Y/N): ").strip().upper()
            if (confirm == "Y"):
                #addIncome
                return new_trans
            else:
                print("Transaction cancelled")
                return None
        except Exception as e:
                print(f"An error occurred: {e}")

    def addIncome(self):
        print("Adding income...")
        income = self.create_transaction(self.income_categories, True)
        if income:
            self.transactions.append(income)
            self.addTransactionCSV(income)
            print(f"Income added! ID:{income.id}")

    def addExpense(self):
        print("Adding an expense...")
        expense = self.create_transaction(self.expense_categories, False)
        if expense:
            self.transactions.append(expense)
            self.addTransactionCSV(expense)
            print(f"Expense added! ID:{expense.id}")

    #----------quickAdd methods----------#
    def quickAdd(self, category, date, amount, desc, is_income):
        #quick add transaction details
        try:
            #creates a date object under the format of DD/MM/YYYY
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            #create a new transaction with details
            new_trans = Transaction(category, date_obj, amount, desc, is_income)
            self.transactions.append(new_trans)
            self.addTransactionCSV(new_trans)
            print(f"{'Income' if is_income else 'Expense'} added! ID: {new_trans.id}")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

    def quickAddIncome(self, date, amount, desc, category = "Misc"):
        #quick add for income, no prompt
        self.quickAdd(category, date, amount, desc, True)

    def quickAddExpense(self, date, amount, desc, category = "Misc"):
        #quick add for expense, no prompt
        self.quickAdd(category, date, amount, desc, False)
    

    #----------listing and searching----------#
    def listTransactions(self):
        #lists all transactions
        if not self.transactions:
            print("\nNo transactions recorded\n")
            return
        print("\n---All transactions---\n")
        for t in self.transactions:
            print(t)

    def findTransaction(self):
        #find a transaction based on attributes
        return

    #----------editing and deleting----------#
    def editTransaction(self, trans_id, new_amount = None, new_desc = None):
        #edits transaction based on ID
        for t in self.transactions:
            if (t.id == trans_id):
                print(f"\nFound transaction:\n{t}")
                if new_amount is not None:
                    t.amount = new_amount 
                if new_desc is not None:
                    t.desc = new_desc 
                print(f"Edited transaction:\n {t}")
                confirm = input("Confirm edit? (Y/N): ").strip().upper()
                if(confirm == "Y"):
                    self.saveAllTransactions()
                    print("Edits made and saved")
                else:
                    print("No edits made")
                return
        print("No transaction found")

    def deleteTransaction(self, trans_id = None, trans_amount = None, trans_desc = None):
        #deletes a transaction based on ID
        for t in self.transactions:
            if t.id == trans_id or t.amount == trans_amount or t.desc == trans_desc:
                try:
                    print(f"\nFound transaction:\n{t}")
                    confirm = input(f"Delete transaction? (Y/N): ").strip().upper()
                    if (confirm == "Y"):
                        self.transactions.remove(t)
                        print(f"Transaction {trans_id} removed")
                        self.saveAllTransactions()
                        return 
                    else:
                        print("No transaction deleted")
                except Exception as e:
                    print(f"An error occurred: {e}")
                return
        print(f"Transaction with {trans_id} not found")

    #----------CSV management----------#
    def addTransactionCSV(self, transaction):
        #adds a transaction to the CSV file
        file_exists = os.path.isfile(self.filename) and os.path.getsize(self.filename) > 0 
        with open(self.filename, mode = "a", newline = "", encoding = "utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["id", "type", "category", "date", "amount", "desc"])
            writer.writerow([
                transaction.id,
                "income" if transaction.is_income else "expense",
                transaction.category,
                transaction.date.strftime("%Y-%m-%d"),
                transaction.amount,
                transaction.desc
                ])

    def loadTransactions(self):
        #load all transactions into self.transactions
        file_exists = os.path.isfile(self.filename) and os.path.getsize(self.filename) > 0
        if not file_exists:
            print("No transactions found. Starting with an empty list.")
            return
        with open(self.filename, mode = "r", newline = "", encoding = "utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    new_trans = Transaction(
                        category = row["category"],
                        date = datetime.strptime(row["date"], "%Y-%m-%d"),
                        amount = float(row["amount"]),
                        desc = row["desc"],
                        is_income = (row["type"] == "income")
                    )
                    new_trans.id = row["id"]
                    self.transactions.append(new_trans)
                except Exception as e:
                    print(f"An error occurred: {e}")
    
    def printAllTransactions(self):
        if not self.transactions:
            print("No transactions exist")
            return
        print("---Transactions---")
        for trans in self.transactions:
            print(trans, end = "\n")

    def clearTransactions(self):
        if not self.transactions:
            print("No transactions exist")
            return
        confirm = input("Are you sure you want to clear all transactions? (Y/N): ").strip().upper()
        if (confirm == "Y"):
            self.transactions.clear()
            self.saveAllTransactions()
            print("All transactions cleared")
        else:
            print("No transactions have been cleared.")

    def saveAllTransactions(self):
        #overwrites csv file with self.transactions
        with open(self.filename, mode = "w", newline = '', encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "type", "category", "date", "amount", "desc"])
            for transaction in self.transactions:
                writer.writerow([
                    transaction.id,
                    "income" if transaction.is_income else "expense",
                    transaction.category,
                    transaction.date.strftime("%Y-%m-%d"),
                    transaction.amount,
                    transaction.desc
                ])