from datetime import date, datetime
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
        trans_str = "Income" if self.is_income == True else "Expense";
        return f"{trans_str} | {self.date.strftime('%Y-%m-%d')} | {self.category} | {self.amount} | {self.desc}";

    def transaction_category(self, categories):
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}");

        while True:
            try:
                menu_selection = int(input(f"Enter your menu selection (1 - {len(categories)})\n")) - 1;
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
                amount = int(input("Enter expense amount: "))
                return amount;
            except ValueError:
                print("Incorrect input. Please enter a valid value")
    
    def transaction_desc(self):
        while True:
            try:
                desc_choice = input("Would you like to enter a description (Y/N): ")
                if desc_choice.strip().upper() == "Y":
                    desc = input("Enter description: ")
                    return desc;
                elif desc_choice.strip().upper() == "N":
                    desc = ""
                    break;
                else:
                    print("Invalid. Please enter Y or N")
            except Exception:
                print("An error occurred")

    #----------Getters and setters----------#
    def getID(self):
        if self.id:
            return self.id
        else:
            return "Error"
    def getCategory(self):
        if self.category:
            return self.category
        else:
            return "Error"
    def getDate(self):
        if self.date:
            return self.date
        else:
            return "Error"
    def getAmount(self):
        if self.amount:
            return self.amount
    def getDesc(self):
        if self.desc:
           return self.desc
        else:
            return "Error"
    def getType(self):
        if (self.is_income):
            return "This is an income"
        else:
            return "This is an expense"