import os
from datetime import datetime as dt
from .finance import Finance
import src.financeStatistics as fs
import src.financeGeneration as fg
import src.personalFunctions as pf


class Menu:

    def __init__(self):
        self.f = Finance()
        self.f.readCSV(self.f.filename)

    def mainMenu(self):
        print("\nWelcome to the Finance Tracker!")
        while True:
            print("\nMain Menu:")
            print("1. View Transactions\n2. Statistics\n3. Modify Transactions\n4. Quit")
            option = self.getUserOption(4)
            match option:
                case 1:
                    self.viewTransactions()
                case 2:
                    self.statsMenu()
                case 3:
                    self.modifyMenu()
                case 4:
                    print("Goodbye!")
                    return

    def getUserOption(self, upper_limit: int) -> int:
        while True:
            try:
                option = int(input(f"Enter your option (1 - {upper_limit}): "))
                if 1 <= option <= upper_limit:
                    return option
                else:
                    print("Invalid option. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def viewTransactions(self):
        print("\nView Transactions Menu")
        while True:
            print("1. All Transactions\n2. All Income\n3. All Expenses\n4. Filter Transactions by Dates\n5. Find Transaction\n6. Main Menu")
            option = self.getUserOption(6)
            match option:
                case 1:
                    self.f.listTransactions()
                case 2:
                    fs.printAllIncomesOrExpenses(self.f, True)
                case 3:
                    fs.printAllIncomesOrExpenses(self.f, False)
                case 4:
                    print(self.fromMenuFilterDates(printing=True))
                case 5:
                    trans_id = input("Enter transaction ID (\"q\" to quit): ").strip()
                    if trans_id == "q":
                        print("Quitting...")
                        break
                    else:
                        t = self.f.findTransaction(trans_id)
                        print(t if t else "Transaction not found.")
                    
                case 6:
                    return

    def statsMenu(self):
        print("\nStatistics Menu")
        while True:
            print("1. Date Functions\n2. Category Functions\n3. Misc Functions\n4. Main Menu")
            option = self.getUserOption(4)
            match option:
                case 1:
                    self.dateStatsMenu()
                case 2:
                    self.categoryStatsMenu()
                case 3:
                    self.miscStatsMenu()
                case 4:
                    return

    def dateStatsMenu(self):
        print("\nDates Menu")
        while True:
            print("1. Filter Records by Dates\n2. Income by Dates\n3. Expenses by Dates\n4. Net Income by Dates\n5. Stats Menu")
            option = self.getUserOption(5)
            match option:
                case 1:
                    print(self.fromMenuFilterDates(printing=True))
                case 2:
                    fs.income_by_dates(self.f)
                case 3:
                    fs.expenses_by_dates(self.f)
                case 4:
                    fs.net_income_by_dates(self.f)
                case 5:
                    return

    def fromMenuFilterDates(self, start=None, end=None, printing=False):
        try:
            start_str = input("Enter the start date (YYYY-MM-DD): ").strip()
            start = dt.strptime(start_str, "%Y-%m-%d")
            end_str = input("Enter the end date (YYYY-MM-DD): ").strip()
            end = dt.strptime(end_str, "%Y-%m-%d")
        except ValueError:
            print("Error occurred: Invalid date format. Use YYYY-MM-DD.")
            return None
        return fs.filter_records_by_dates(self.f, start, end,printing)

    def categoryStatsMenu(self):
        print("\nCategory Menu")
        while True:
            print("1. Most Common Categories\n2. Amounts by Category\n3. Stats Menu")
            option = self.getUserOption(3)
            match option:
                case 1:
                    fs.most_common_categories(self.f)
                case 2:
                    fs.amount_by_category(self.f)
                case 3:
                    return

    def miscStatsMenu(self):
        print("\nMisc Menu")
        while True:
            print("1. Custom remove rows function\n2. Stats Menu")
            option = self.getUserOption(2)
            match option:
                case 1:
                    pf.removeUnwantedRows(self.f)
                case 2:
                    return

    def modifyMenu(self):
        print("\nModification Menu")
        while True:
            print(
                "1. Add New Items from Statement\n"
                "2. Add Transaction Manually\n"
                "3. Delete All Transactions\n"
                "4. Delete a Single Transaction\n"
                "5. Edit Transaction\n"
                "6. List All Transactions\n"
                "7. Generate Sample Transactions\n"
                "8. Personal Removal\n"
                "9. Save Changes\n"
                "10. Main Menu"
            )
            option = self.getUserOption(10)
            match option:
                case 1:
                    self.statementInput()

                case 2:
                    try:
                        t_type = input("Is this Income? (y/n): ").strip().lower() == "y"
                        amount = float(input("Amount: "))
                        cat = input("Category: ").strip()
                        date_str = input("Date (YYYY-MM-DD): ").strip()
                        desc = input("Description: ").strip()
                        self.f.addTransaction(t_type, amount, cat, date_str, desc)
                    except ValueError as e:
                        print(f"Invalid input: {e}")

                case 3:
                    confirm = input("Are you sure you want to delete ALL transactions? (y/n): ").strip().lower()
                    if confirm == 'y':
                        if hasattr(self.f, "clearTransactions"):
                            self.f.clearTransactions()
                        else:
                            self.f.transactions.clear()
                        print("All transactions cleared.")

                case 4:
                    trans_id = input("Enter Transaction ID to delete: ").strip()
                    self.f.deleteTransaction(trans_id)

                case 5:
                    trans_id = input("Enter Transaction ID to edit: ").strip()
                    attr = input("Attribute to edit (type, amount, category, date, description): ").strip()
                    val = input("New Value: ").strip()
                    if attr.lower() == "type":
                        val = val.lower() in ["true", "y", "income", "yes"]
                    elif attr.lower() == "amount":
                        try:
                            val = float(val)
                        except ValueError:
                            print("Invalid amount numeric format.")
                            continue
                    self.f.editTransaction(trans_id, attr, val)

                case 6:
                    self.f.listTransactions()

                case 7:
                    self.f.transactions.extend(fg.generate_sample_income())
                    self.f.transactions.extend(fg.generate_sample_expenses())
                    self.f.saveToCSV()
                    print("Sample transactions generated and saved.")

                case 8:
                    pf.removeUnwantedRows(self.f)
                    print("Personal removal complete.")

                case 9:
                    self.f.saveToCSV()
                    print("Changes saved successfully.")

                case 10:
                    self.f.saveToCSV()
                    return  # Returns back to mainMenu loop safely

    def statementInput(self):
        while True:
            path = input("Please enter the statement file's path (\"q\" to quit): ").strip()
            if path.lower() == "q":
                break
            elif not os.path.exists(path):
                print("Couldn't find the file.")
            else:
                try:
                    new_transactions = fg.CSVStatementConverter(path)
                    self.f.transactions.extend(new_transactions)
                    self.f.saveToCSV()
                    print(f"Successfully loaded {len(new_transactions)} transactions.")
                    break
                except Exception as e:
                    print(f"An error occurred while importing: {e}")


if __name__ == "__main__":
    m = Menu()
    m.mainMenu()