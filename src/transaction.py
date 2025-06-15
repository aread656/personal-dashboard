import datetime
import uuid

class Transaction:
    def __init__(self, category, date, amount, desc, is_income):
        self.id = str(uuid.uuid4()); 
        self.category = category
        self.date = date
        self.amount = amount
        self.desc = desc
        self.is_income = is_income

    def __str__(self):
        trans_str = "Transaction Details:\n"
        return;

    def transaction_category(self, categories):
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}");

        while True:
            try:
                menu_selection = int(input(f"Enter your menu selection (1 - {len(categories)})\n"))
                if 1 <= menu_selection <= len(categories):
                    return (categories[menu_selection])
                else:
                    print("Out of bounds")
            except ValueError:
                print("Invalid input. Try again.")
            except IndexError:
                print("That number isn't an option here. Please try again.")

    def transaction_date(self):
        while True:
            date_str = input("Enter a date (YYYY-MM-DD)");
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
                break;
            except ValueError:
                print("Incorrect date format. Please use YYYY-MM-DD format")

    def transaction_amount(self):
        while True:
            try:
                amount = int(input("Enter expense amount"))
                break;
            except ValueError:
                print("Incorrect input. Please enter a valid value")
    
    def transaction_desc(self):
        while True:
            try:
                desc_choice = input("Would you like to enter a description (Y/N): ")
                if desc_choice.strip().upper() == "Y":
                    desc = input("Enter description: ")
                    break;
                elif desc_choice.strip().upper() == "N":
                    desc = ""
                    break;
                else:
                    print("Invalid. Please enter Y or N")
            except Exception:
                print("An error occurred")