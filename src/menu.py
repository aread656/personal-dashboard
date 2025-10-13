from financeTracker import Finances
import financeStatistics as fs
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
        return