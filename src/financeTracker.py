import csv
from genericpath import exists
import os
from datetime import datetime
from transaction import Transaction

class Finances:
    #a class which will manage a collection of transactions
    #the class will allow for adding, editing, and removing csv file records

    #a list of all income and expense categories:
    income_categories = ["Pay", "Gift", "Dividend", "Loans", "Misc"]
    expense_categories = ["Bills", "Fuel", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Misc"]

    def __init__(self, filename = "transactions.csv"):
        #initialise a finance class instance
        self.filename = filename
        self.balance = 0;
        self.transactions = []
        self.loadTransactions()
        return;

    #-------------Adding Income/Expenses----------------#
    def create_transaction(self, categories, is_income):
        #prompt the user to input transaction details
        category = Transaction.transaction_category(self, categories);
        date = Transaction.transaction_date()
        amount = Transaction.transaction_amount()
        desc = Transaction.transaction_desc();
        
        new_trans = Transaction(category, date, amount, desc, is_income)
        #check user if the transaction details are correct
        print("Please check the details of your transaction...\n")
        try:
            print(f"{new_trans}")
            confirm = input("Confirm transaction details? (Y/N)").strip().upper()
            if (confirm == "Y"):
                #addIncome
                return new_trans;
            else:
                print("Transaction cancelled")
                return;
        except Exception as e:
                print(f"An error occurred: {e}")
        return;
    def addIncome(self):
        print("Adding income...")
        income = self.create_transaction(self, self.income_categories, True)
        if income:
            self.transactions.append(income)
            self.addTransactionCSV(income)
            print(f"Income added! ID:{income.getID}")
        return;
    def addExpense(self):
        #add an expense using a CLI
        print("Adding an expense...")
        expense = self.create_transaction(self, self.expense_categories, False)
        if expense:
            self.transactions.append(expense)
            self.addTransactionCSV(expense)
            print(f"Expense added! ID:{expense.getID}")
        return;

    #----------quickAdd methods----------#
    def quickAdd(self, category, date, amount, desc, is_income):
        #quick add transaction details
        try:
            #creates a date object under the format of YYYY-MM-DD
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            #create a new transaction with details
            new_trans = Transaction(category, date_obj, amount, desc, is_income)
            self.transactions.append(new_trans)
            self.addTransactionCSV(new_trans)
            print(f"{"Income" if is_income else "Expense"} added!")
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
            print("No transactions recorded")
            return;
        print("All transactions:\n")
        for t in self.transactions:
            print(t)
    def findTransaction(self):
        #find a transaction based on attributes
        return;

    #----------editing and deleting----------#
    def editTransaction(self, trans_id, new_amount = None, new_desc = None):
        #edits transaction based on ID
        for t in self.transactions:
            if (t.id == trans_id):
                if t.amount is not None:
                    t.amount = new_amount;
                if t.desc is not None:
                    t.desc = new_desc;
                print(f"Edited transaction:\n {t}")
                confirm = input("Confirm edit? (Y/N)").strip().upper()
                if(confirm == "Y"):
                    self.saveAllTransactions()
                else:
                    print("No edits made")
                return;
            else:
                print("No transaction found")

    def deleteTransaction(self, trans_id):
        #deletes a transaction based on ID
        for t in self.transactions:
            if t.id == trans_id:
                try:
                    confirm = input(f"Delete transaction? (Y/N)").strip().upper()
                    if (confirm == "Y"):
                        self.transactions.remove(t)
                        print(f"Transaction {trans_id} removed")
                        self.saveAllTransactions()
                        return;
                    else:
                        print("No transaction deleted")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print(f"Transaction is {trans_id} not found")

    #----------CSV management----------#
    def addTransactionCSV(self, transaction):
        #adds a transaction to the CSV file
        #check that the file exists and has length > 0
        file_exists = os.path.isfile(self.filename) and os.path.getsize(self.filename) > 0;
        #open file and establish csv writer
        with open(self.filename, mode = "a", newline = "", encoding = "utf-8") as f:
            writer = csv.writer(f)
        #create headers if the csv does not exist, establishing header order
        if not file_exists:
            writer.writero(["ID", "Type", "Category", "Date", "Amount", "Desc"])
        #use writer to input attributes
        writer.writerow([
            transaction.id,
            "Income" if transaction.is_income else "Expense",
            transaction.category,
            transaction.date,
            transaction.amount,
            transaction.desc
            ])
        return;
    def loadTransactions(self):
        #load all transactions into self.transactions
        return;
    def saveAllTransactions(self):
        #saves all transactions to the CSV file
        return;

"""to be implemented:
1. searching methods by each attribute of the transactions in the file
2. deleting transactions
3. editing transactions"""