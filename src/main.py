import financeGeneration as fg
import financeStatistics as fs
import personalFunctions as pf
from financeTracker import Finances
from menu import Menu

finances = Finances()

"""finances.clearTransactions()

finances.transactions = fg.CSVStatementConverter("Statement Jan-Jun 25.csv")
finances.printAllTransactions()
finances.saveAllTransactions()

finances.clearTransactions()
finances.transactions.extend(fg.generate_student_income())
finances.transactions.extend(fg.generate_student_expenses())
finances.printAllTransactions()
finances.saveAllTransactions()

pf.removeUnwantedRows(finances)
fs.printAllIncomesOrExpenses(finances, True)
print("\n\n")
fs.printAllIncomesOrExpenses(finances, False)

fs.incomeByDates(finances)
fs.expensesByDates(finances)
fs.netIncomeByDates(finances)

fs.mostCommonCategories(finances)
fs.amountsByCategory(finances)

print(fs.filterRecordsByDates(finances, "2025-03-01", "2025-03-31"))
"""

m = Menu()
m.displayMainMenu()