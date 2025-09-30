from financeTracker import Finances
import financeStatistics as fs
class Menu:

    def __init__(self):
        self.f = Finances()

    def displayMainMenu(self):
        OPTIONS_MAP = {
            1:self.viewTransactions,
            2:lambda: print("Stats Menu"),
            3:lambda: print("Modification Menu")
        }
        cont = True
        print("Welcome to the Finance Tracker!")
        while(cont):
            print("Options:")
            print("1: View Transactions\n2: Statistics\n3: Modify Transactions")
            option = self.getUserOption(3)
            func = OPTIONS_MAP.get(option)
            if func:
                func()
            else:
                continue
            """match (option):
                case 1:
                    self.viewTransactions()
                    cont = False
                    return
                case 2:
                    self.displayMainMenu()
                case 3:
                    self.displayMainMenu()"""
            #1: view all transactions
            #2: statistics
            #3: modify transactions
        return
    def getUserOption(self, upper_limit) -> int:
        cont = True
        try:
            option = int(input(f"Enter your option: 1 - {upper_limit}: "))
            if (1 <= option <= upper_limit):
                print("Yes")
                cont = False
            else:
                print("Invalid option. Try again.")
        except Exception:
            print("Invalid input. Try again")
        return option
    
    def viewTransactions(self):
        OPTIONS_MAP = {
            "1" : lambda: self.f.listTransactions(),
            "2" : lambda: fs.printAllIncomesOrExpenses(self.f, True),
            "3" : lambda: fs.printAllIncomesOrExpenses(self.f, False),
            "4" : lambda: print("Under construction"),
            "5" : lambda: self.displayMainMenu()
        }
        cont = True
        print("View Transactions Menu")
        while(cont):
            print("1. All Transactions\n2: All Income\n3. All Expenses\n4: Filter Transactions by Dates\n5: Main Menu")
            option = self.getUserOption(5)
            func = OPTIONS_MAP.get(option)
            if func:
                func()