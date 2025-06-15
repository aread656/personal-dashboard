from datetime import datetime

class finances:
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

    def select_expense_category(self):
        for i, category in enumerate(self.expense_categories):
            print(f"{i + 1}. {category}");

        #select menu option
        while True:
            try:
                menu_selection = int(input(f"Enter your menu selection (1 - {len(self.expense_categories)})"))
                if 1 <= menu_selection <= (len(self.expense_categories) - 1):
                    return (self.expense_categories[menu_selection] - 1)
                break;
            except ValueError:
                print("Invalid input. Try again.")
            except IndexError:
                print("That number isn't an option here. Please try again.")

    def select_transaction_date(self):
        while True:
            date_str = input("Enter a date (YYYY-MM-DD)");
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
                break;
            except ValueError:
                print("Incorrect date format. Please use YYYY-MM-DD format")
    
    def addExpense(self):
        #adds a transaction with category, date, amount, description
        #build a menu to choose category
        print("Adding an expense...\n")
        
        #select category
        category = self.select_expense_category();

        #select date
        date = self.select_transaction_date();

        #select amount

        #enter description
        desc_choice = input("Would you like to enter a description (Y/N): ")

        #add to csv file
        return;





