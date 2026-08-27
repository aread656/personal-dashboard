INCOME_CATEGORIES = ["Pay", "Gift", "Dividend", "Loans", "Transfer", "Misc"]
EXPENSE_CATEGORIES = ["Bills", "Transport", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Transfer", "Savings", "Misc"]

CATEGORY_MAP = {
    ("Salary and pension", "Salary / wages"): "Pay",
    ("Salary and pension","Student loan"):"Loans",
    ("Pension, savings and investment","Savings"):"Savings",

    ("Household goods","Supermarket"):"Groceries",
    ("Household goods","Other"):"Groceries",

    ("Transport", "Fuel"): "Transport",
    ("Transport", "Bus / train"): "Transport",
    ("Transport", "Plane"): "Leisure",
    ("Transport", "Parking"): "Transport",
    
    ("Recreation and leisure", "Caf� / restaurant"): "Leisure",
    ("Recreation and leisure", "Bar / nightclub"): "Leisure",
    ("Recreation and leisure", "Cinema / concert / theatre"): "Leisure",
    ("Recreation and leisure", "Holiday"): "Leisure",
    ("Recreation and leisure", "Games / toys"): "Leisure",
    
    ("Uncategorised","Uncategorised"):"Misc",
    
    ("Recreation and leisure","Other"):"Leisure",
    
    ("Housing", "Maintenance"): "Bills",
    ("Housing", "Other"): "Bills",

    ("Clothing, shoes and personal care", "Clothing / shoes"): "Clothing",
    ("Clothing, shoes and personal care", "Personal care"): "Clothing",

    ("Other income","Own account transfer"):"Transfer",
    ("Other income","Other transfers"):"Misc",
    ("Other expenses","Fees"):"Misc",
    ("Other expenses", "Donations"): "Charity",
    ("Other expenses", "Cash withdrawals"): "Misc",
}