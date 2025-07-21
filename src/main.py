import manager
import financeUtilities as fu

mgr = manager.Manager()
mgr.test()
#test success of generate_student_income
finances = mgr.financeTracker
if finances.transactions:
    finances.clearTransactions()
generated_income = fu.generate_student_income()
generated_expenses = fu.generate_student_expenses()
finances.transactions.extend(generated_income)
finances.transactions.extend(generated_expenses)
finances.printAllTransactions()
finances.saveAllTransactions()