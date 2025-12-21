from datetime import date, datetime
import uuid

class Transaction:
    def __init__(self, category, date, amount, desc, is_income):
        self.id = str(uuid.uuid4().hex[:8]) 
        self.category = category

        if isinstance(date, str):
            try:
                self.date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect date string format, expected YYYY-MM-DD")
        else: self.date = date
        
        self.amount = amount
        self.desc = desc
        self.is_income = is_income

    def __str__(self):
        trans_str = "Income" if self.is_income == True else "Expense"
        return f"{trans_str} | {self.date.strftime('%d/%m/%Y')} | {self.category} | {self.amount} | {self.desc}";

    def transaction_category(self, categories):
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}")

        while True:
            try:
                menu_selection = int(input(f"Enter your menu selection (1 - {len(categories)})\n"));
                if 1 <= menu_selection <= len(categories):
                    return (categories[menu_selection - 1])
                else:
                    print("Out of bounds")
            except ValueError:
                print("Invalid input. Try again.")
            except IndexError:
                print("That number isn't an option here. Please try again.")

    def transaction_date(self):
        while True:
            date_str = input("Enter a date (YYYY-MM-DD): ")
            try:
                return datetime.strptime(date_str, "%Y/%m/%d")
            except ValueError:
                print("Incorrect date format. Please use YYYY-MM-DD format")

    def transaction_amount(self):
        while True:
            try:
                amount = float(input("Enter transaction amount: "))
                return amount
            except ValueError:
                print("Incorrect input. Please enter a valid value")
    
    def transaction_desc(self):
        while True:
            try:
                desc_choice = input("Would you like to enter a description (Y/N): ")
                if desc_choice.strip().upper() == "Y":
                    desc = input("Enter description: ")
                    return desc
                elif desc_choice.strip().upper() == "N":
                    desc = ""
                    break
                else:
                    print("Invalid. Please enter Y or N")
            except Exception as e:
                print("An error occurred: " + e)

    def transaction_type(self):
        while True:
            try:
                type_choice = input("Is this an expense or an income? (I/E)")
                if type_choice.strip().upper() == "I":
                    return True
                return False
            except Exception as e:
                print("An error occurred: " + e)