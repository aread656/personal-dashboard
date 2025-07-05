from financeTracker import Finances
def loadSampleData(financeTracker):
    financeTracker.quickAddIncome("2025-07-03", 200, "Month's Salary", "Pay")
    financeTracker.quickAddExpense("2025-07-04", 50, "Electric Bill", "Bills")
    financeTracker.quickAddExpense("2025-07-05", 20, "Bowling", "Leisure")
