import manager
mgr = manager.Manager()
mgr.test();
mgr.financeTracker.clearTransactions();
mgr.financeTracker.quickAddExpense('2020-01-01', 1000, "")
mgr.financeTracker.quickAddExpense('2020-01-01', 1000, "")
mgr.financeTracker.loadTransactions();
