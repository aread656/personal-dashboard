from datetime import datetime

class finances:
    #add into code the relevant categories for adding excpeses and income. Establish transaction to finances relationship
    expense_categories = ["Groceries", "Fuel", "Gifts", "Charity", "Household", "Rent", "Bills", "Misc"]
    income_categories = ["Salary", "Gifts", "Dividends", "Student Loans", "Side Hustles"]

    def __init__(self, pay):
        self.week_pay = pay
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
        #add category, date, amount, description
        print("Adding an income source...\n")
        category = self.income_category();
        date = self.transaction_date();
        return;

    def addExpense(self):
        #adds a transaction with category, date, amount, description
        #build a menu to choose category
        print("Adding an expense...\n")
        #select category
        category = self.expense_category();
        #select date
        date = self.transaction_date();
        #select amount
        while True:
            try:
                amount = int(input("Enter expense amount"))
                break;
            except ValueError:
                print("Incorrect input. Please enter a valid value")
        #enter description
        while True:
            try:
                desc_choice = input("Would you like to enter a description (Y/N): ")
                if desc_choice.capitalize == "Y":
                    desc = input("Enter description: ")
                    break;
                elif desc_choice.capitalize == "N":
                    desc == ""
                    break;
                else:
                    print("Invalid. Please enter Y or N")
            except Exception:
                print("An error occurred")

        #add to csv file
        return;





