import manager
import financeGeneration as fg

mgr = manager.Manager()
finances = mgr.financeTracker
"""if finances.transactions:
    finances.clearTransactions()
generated_income = fg.generate_student_income()
generated_expenses = fg.generate_student_expenses()
finances.transactions.extend(generated_income)
finances.transactions.extend(generated_expenses)
finances.printAllTransactions()
finances.saveAllTransactions()"""

finances.transactions.append(fg.CSVStatementConverter())
finances.printAllTransactions()