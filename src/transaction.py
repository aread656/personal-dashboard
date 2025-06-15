import datetime

class transaction:
    id_count = 1;

    def __init__(self, category, date, amount, desc):
        self.id = transaction.id_count + 1
        self.category = category
        self.date = date
        self.amount = amount
        self.desc = desc
        return;
    def __str__(self):
        trans_str = "Transaction Details:\n"
        return;

    def income_category(self, categories):
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}");

        #select menu option
        while True:
            try:
                menu_selection = int(input(f"Enter your menu selection (1 - {len(categories)})"))
                if 1 <= menu_selection <= (len(categories) - 1):
                    return (categories[menu_selection] - 1)
                break;
            except ValueError:
                print("Invalid input. Try again.")
            except IndexError:
                print("That number isn't an option here. Please try again.")

    """def expense_category(self):
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
                print("That number isn't an option here. Please try again.")"""

    def transaction_date(self):
        while True:
            date_str = input("Enter a date (YYYY-MM-DD)");
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
                break;
            except ValueError:
                print("Incorrect date format. Please use YYYY-MM-DD format")