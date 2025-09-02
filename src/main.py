import manager
import financeGeneration as fg
import financeStatistics as fs

mgr = manager.Manager()
finances = mgr.financeTracker
fs.incomeByDates(finances)
fs.expensesByDates(finances)
