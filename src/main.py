import manager
import financeGeneration as fg
import financeStatistics as fs

mgr = manager.Manager()
finances = mgr.financeTracker

"""finances.clearTransactions()
finances.transactions = fg.CSVStatementConverter("Statement Jan-Jun 25.csv")
finances.printAllTransactions()
finances.saveAllTransactions()"""

"""fs.incomeByDates(finances)
fs.expensesByDates(finances)
fs.netIncomeByDates(finances)"""

fs.mostCommonCategories(finances)
fs.amountsByCategory(finances)