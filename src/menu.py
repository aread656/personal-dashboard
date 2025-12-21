from financeTracker import Finances
import financeStatistics as fs
import financeGeneration as fg
import os
class Menu:

    def __init__(self):
        self.f = Finances()

    def mainMenu(self):
        print("\nWelcome to the Finance Tracker!")
        while(True):
            print("Main Menu:")
            print("1. View Transactions\n2. Statistics\n3. Modify Transactions\n4. Quit")
            option = self.getUserOption(4)
            match (option):
                case 1:
                    self.viewTransactions()
                    cont = False
                case 2:
                    self.statsMenu()
                case 3:
                    self.modifyMenu()
                case 4:
                    print("Goodbye!")
                    return
    def getUserOption(self, upper_limit) -> int:
        while(True):
            try:
                option = int(input(f"Enter your option: 1 - {upper_limit}: "))
                if (1 <= option <= upper_limit):
                    return option
                else:
                    print("Invalid option. Try again.")
            except Exception:
                print("Invalid input. Try again")
    
    def viewTransactions(self):
        print("View Transactions Menu")
        while(True):
            print("1. All Transactions\n2: All Income\n3. All Expenses\n4: Filter Transactions by Dates\n5: Main Menu")
            option = self.getUserOption(5)
            match(option):
                case 1:
                    self.f.listTransactions()
                case 2:
                    fs.printAllIncomesOrExpenses(self.f, True)
                case 3:
                    fs.printAllIncomesOrExpenses(self.f, False)
                case 4:
                    print("Under construction")
                case 5:
                    return

    def statsMenu(self):
        print("Statistics Menu")
        while(True):
            print("1. Date Functions\n2. Category Functions" \
            "\n3. Misc Functions\n4. Main Menu")
            option = self.getUserOption(4)
            match(option):
                case 1:
                    self.dateStatsMenu()
                case 2:
                    self.categoryStatsMenu()
                case 3:
                    self.miscStatsMenu()
                case 4:
                    return
    def dateStatsMenu(self):
        print("\nDates menu")
        print("1. Filter Records by Dates\n2. Income by Dates\n3. Expenses by Dates" \
        "\n4. Net Income by Dates\n5. Stats Menu")
        option = self.getUserOption(5)
        match(option):
            case 1:
                print("Under construction")
            case 2:
                fs.incomeByDates(self.f)
            case 3:
                fs.expensesByDates(self.f)
            case 4:
                fs.netIncomeByDates(self.f)
            case 5:
                return
    def categoryStatsMenu(self):
        print("Category Menu")
        print("1. Most Common Categories\n2. Amounts by Category\n3. Stats Menu")
        option = self.getUserOption(3)
        match(option):
            case 1:
                fs.mostCommonCategories(self.f)
            case 2:
                fs.amountsByCategory(self.f)
            case 3:
                return
    def miscStatsMenu(self):
        print("Misc menu")
        return

    def modifyMenu(self):
        print("Modification Menu")
        while(True):
            print("1. Add New Items from Statement\n2. Add Transaction Manually\n3. Delete All Transactions" \
            "\n4. Delete a Single Transaction\n5. Edit Transaction\n6. List All Transactions\n" \
            "7. Generate Sample Transactions\n8. Save Changes\n9. Main Menu")
            option = self.getUserOption(7)
            match(option):
                case 1:
                    return
                case 2:
                    self.f.addTransactionCSV(self.f.create_transaction())
                    return
                case 3:
                    self.f.clearTransactions()
                    return
                case 4:
                    self.f.deleteTransaction()
                    return
                case 5:
                    self.f.editTransaction()
                    return
                case 6:
                    self.f.listTransactions()
                    return
                case 7:
                    fg.generate_sample_income()
                    fg.generate_sample_expenses()
                    return
                case 8:
                    self.mainMenu()
                    return
        return
    def statementInput(self):
        while(True):
            try:
                path = input("Please enter the statement file's path")
                if not os.path.exists(path):
                    print("Couldn't find the file")
                else:
                    fg.CSVStatementConverter(path)
            except Exception as e:
                print("An error occurred: "+e)

def main():
    m = Menu()
    m.mainMenu()

if __name__ == "__main__":
    main()