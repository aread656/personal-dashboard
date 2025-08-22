import manager
import financeGeneration as fg
import financeStatistics as fs

mgr = manager.Manager()
finances = mgr.financeTracker
finances.clearTransactions()
finances.transactions.extend(fg.CSVStatementConverter(filename = "Statement Jan-Jun 25.csv"))
#finances.printAllTransactions()
finances.saveAllTransactions()
"""print(fs.totalIncome(finances))
print(fs.totalExpenses(finances))
print(fs.netIncome(finances))
print(finances.getAllTransactions())"""
print(fs.incomeByDates(finances))