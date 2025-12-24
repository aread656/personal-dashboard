import csv
import os
from datetime import datetime
from transaction import Transaction

class Finances:
    #a class which will manage a collection of transactions
    #the class will allow for adding, editing, and removing records

    #a list of all income and expense categories:
    income_categories = ["Pay", "Gift", "Dividend", "Loans", "Misc"]
    expense_categories = ["Bills", "Fuel", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Misc"]

    def __init__(self, filename = "financeRecords.csv"):
        #initialise a finance class instance
        self.filename = filename
        self.balance = 0 
        self.transactions = []
        self.loadTransactions()

    #-------------Getters for Finances() class-----------------#
    def getAllTransactions(self):
        return self.transactions
    
    #-------------Adding Income/Expenses with CLI----------------#
    def create_transaction(self):
        #prompt the user to input transaction details
        is_income = Transaction.transaction_type(self)
        if is_income:
            category = Transaction.transaction_category(self, self.income_categories) 
        else:
            category = Transaction.transaction_category(self,self.expense_categories)

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
                self.transactions.append(new_trans)
                self.saveAllTransactions()
                return
            else:
                print("Transaction cancelled")
                return None
        except Exception as e:
                print(f"An error occurred: {e}")
    
    #----------listing and searching----------#
    def listTransactions(self):
        #lists all transactions
        if not self.transactions:
            print("\nNo transactions recorded\n")
            return
        print("\n---All transactions---\n")
        for t in self.transactions:
            print(t)
    def findTransaction(self)->Transaction:
        #find a transaction based on ID
         while(True):
            try:
                selection = input("Enter the transaction's ID, enter \"L\" to list all transactions: ")
                if (selection.strip().upper() == "L"):
                    self.listTransactions()
                else:
                    for t in self.transactions:
                        if (t.id == selection): return t
            except Exception:
                print("An error occurred. Matching transaction not found"); return None
            
    #----------editing and deleting----------#
    def editTransaction(self, trans_id):
        #edits transaction based on ID
        trans = None
        for t in self.transactions:
            if (t.id == trans_id):
                trans = t
                print(f"\nFound transaction:\n{trans}")
                break
        if trans is None:
            print(f"Transaction with id {trans_id} not found"); return
        new_amount = new_desc = new_date = new_cat = new_type = None

        attribute = input("Enter the attribute to edit (date, category, type, amount, or desc): ").strip().lower()
        match(attribute):
            case "date":
                new_date = Transaction.transaction_date(self)
            case "category":
                new_cat = Transaction.transaction_category(self)
            case "type":
                new_type = Transaction.transaction_type(self)
            case "amount":
                new_amount = Transaction.transaction_amount(self)
            case "desc":
                new_desc = Transaction.transaction_desc(self)
            case _:
                print("Invalid. Please try again"); return

        if new_amount is not None: print(f"New amount: {new_amount}") 
        if new_date is not None: print(f"New date: {new_date}") 
        if new_cat is not None: print(f"New category: {new_cat}") 
        if new_type is not None: print(f"New type: {new_type}") 
        if new_desc is not None: print(f"New desc: {new_desc}")  

        confirm = input("Confirm edit? (Y/N): ").strip().upper()
        if(confirm == "Y"):
            if new_amount is not None: trans.amount = new_amount 
            if new_date is not None: trans.date = new_date
            if new_cat is not None: trans.category = new_cat
            if new_type is not None: trans.is_income = new_type
            if new_desc is not None: trans.desc = new_desc 
            self.saveAllTransactions()
            print("Edits made and saved")
        else:
            print("No edits made")
    def deleteTransaction(self, trans_id = None):
        #deletes a transaction based on ID
        for t in self.transactions:
            if t.id == trans_id:
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