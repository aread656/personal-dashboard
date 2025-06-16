from datetime import datetime
from transaction import Transaction

class Finances:
    expense_categories = ["Groceries", "Fuel", "Gifts", "Charity", "Household", "Rent", "Bills", "Misc"]
    income_categories = ["Salary", "Gifts", "Dividends", "Student Loans", "Side Hustles"]

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
            print("Added expense successfully!\n")
        else:
            print("Transaction cancelled")
        #add to csv file
        return;

    def getAllTransactions(self):
        for t in self.transactions:
            print(self.transactions[t])
        return;

    def addTransactionCSV(self):
        return;