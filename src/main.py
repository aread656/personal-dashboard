import manager
import financeGeneration as fg

mgr = manager.Manager()
finances = mgr.financeTracker

finances.clearTransactions()
finances.transactions.extend(fg.CSVStatementConverter())
finances.printAllTransactions()
finances.saveAllTransactions()