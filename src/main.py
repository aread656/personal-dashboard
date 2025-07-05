import manager
import financeUtilities

mgr = manager.Manager()
mgr.test()
"""mgr.financeTracker.addIncome()
mgr.financeTracker.addExpense()
mgr.financeTracker.saveAllTransactions()"""
mgr.financeTracker.clearTransactions()
financeUtilities.loadSampleData(mgr.financeTracker)
mgr.financeTracker.listTransactions()
mgr.financeTracker.saveAllTransactions()