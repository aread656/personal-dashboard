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
    def addExpense(self):
        #select the category of the expense
        #provide the cost of the expense
        return
    def addIncome(self):
        #select income category
        #provide amount of income
        return
    def select_expense_category(self):
        print("Select expense category:")
        for i, category in enumerate(self.expense_categories):
            print(f"{i}: {category}")
        while True:
            try:
                menu_selection = int(input("Enter a number for selection: "))
                if 0 <= menu_selection < len(self.expense_categories):
                    return self.expense_categories[menu_selection]
                else:
                    print("Invalid selection, try again")
            except ValueError:
                print("Enter a valid number")




