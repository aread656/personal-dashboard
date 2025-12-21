from datetime import datetime, timedelta
import csv
import random
from transaction import Transaction

income_categories = ["Pay", "Gift", "Dividend", "Loans", "Misc"]
expense_categories = ["Bills", "Fuel", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Misc"]

CATEGORY_MAP = {("Salary and pension", "Salary / wages"): "Pay",
        ("Other income", "Own account transfer"): "Loans",
        ("Other income", "Other transfers"): "Gift",
        
        ("Transport", "Fuel"): "Fuel",
        ("Transport", "Bus / train"): "Bills",
        ("Transport", "Plane"): "Leisure",
        ("Transport", "Parking"): "Bills",

        ("Household goods", "Supermarket"): "Groceries",
        ("Household goods", "Other"): "Groceries",
        ("Household goods", None): "Groceries",

        ("Recreation and leisure", "Caf� / restaurant"): "Leisure",
        ("Recreation and leisure", "Bar / nightclub"): "Leisure",
        ("Recreation and leisure", "Cinema / concert / theatre"): "Leisure",
        ("Recreation and leisure", "Holiday"): "Leisure",
        ("Recreation and leisure", "Games / toys"): "Leisure",

        ("Other expenses", "Donations"): "Charity",
        ("Other expenses", "Cash withdrawals"): "Misc",
        ("Other expenses", "Own account transfer"): "Misc",

        ("Clothing, shoes and personal care", "Clothing / shoes"): "Clothing",
        ("Clothing, shoes and personal care", "Personal care"): "Clothing",

        ("Housing", "Maintenance"): "Bills",
        ("Housing", "Other"): "Bills",

        ("Uncategorised", "Uncategorised"): "Misc",
    }

def random_dates(start, end):
    delta = end - start
    return (start + timedelta(days = random.randint(0, delta.days))).strftime("%Y-%m-%d")

def generate_sample_income(n = 50):
    transactions = []
    start_date = datetime.now() - timedelta(days = 365)
    end_date = datetime.now()
    for i in range(n):
        category = random.choices(
            population = income_categories,
            weights = [50, 20, 8, 2, 20],
            k = 1
        )[0]
        match category:
            case "Pay":
                amount = round(random.uniform(80, 300), 2)
                description = "Part-time job"
            case "Gift":
                amount = round(random.uniform(20, 40), 2)
                description = "Gifts from family/friends"
            case "Dividend":
                amount = round(random.uniform(0.1, 5), 2)
                description = "Stock dividends"
            case "Loans":
                amount = round(random.uniform(1200, 2000), 2)
                description = "Student Loans"
            case "Misc":
                amount = round(random.uniform(2, 20), 2)
                description = "Miscellaneous"
        date = random_dates(start_date, end_date)
        new_trans = Transaction(
            category = category,
            date = date,
            amount = amount,
            desc = description,
            is_income = True
        )
        transactions.append(new_trans)
    return transactions
    
def generate_sample_expenses(n = 150):
    transactions = []
    start = datetime.now() - timedelta(days = 365)
    end = datetime.now()
    for i in range(n):
        category = random.choices(
            population = expense_categories,
            weights = [5, 10, 30, 5, 10, 2, 15, 20],
            k = 1
        )[0]
        match category:
            case "Bills":
                amount = round(random.uniform(420, 450), 2)
                description = "Monthly rent and bills"
            case "Fuel":
                amount = round(random.uniform(30, 70), 2)
                description = "Car fuel"
            case "Groceries":
                amount = round(random.uniform(15, 40), 2)
                description = "Groceries"
            case "Clothing":
                amount = round(random.uniform(15, 40), 2)
                description = "Clothing"
            case "Charity":
                amount = round(random.uniform(15, 30), 2)
                description = "Foodbank/charity donation"
            case "Emergency":
                amount = round(random.uniform(75, 300), 2)
                description = "Emergency repairs/purchases"
            case "Leisure":
                amount = round(random.uniform(10, 25), 2)
                description = "Entertainment and Leisure"
            case "Misc":
                amount = round(random.uniform(5, 20), 2)
                description = "Other miscellaneous"
        date = random_dates(start, end)
        new_trans = Transaction(
            category = category,
            date = date,
            amount = amount,
            desc = description,
            is_income = False
        )
        transactions.append(new_trans)
    return transactions

def CSVStatementConverter(filename, output = "financeRecords.csv"):
    output_rows = []
    with open(file = filename, mode = "r", encoding = "cp1252", newline = "") as f:
        reader = csv.DictReader(f)
        for line in reader:
            #remove unecessary categories
            line.pop("Reconciled", None)
            line.pop("Status", None)
            line.pop("Balance", None)

            #create is_income attribute for each row
            amount_str = line["Amount"].replace(",", "").strip()
            line["is_income"] = float(amount_str) > 0
            line["Amount"] = abs(float(amount_str))

            #adjust categories to match above categories
            category_key = (line.get("Category"), line.get("Subcategory"))
            mapped = CATEGORY_MAP.get(category_key)

            if not mapped:
                line["Category"] = "Misc"
            else:
                line["Category"] = mapped
            
            line.pop("Subcategory", None)

            #adjust dates into YYYY/MM/DD format
            dt = datetime.strptime(line["Date"], "%m/%d/%Y")
            line["Date"] = dt.strftime("%Y-%m-%d")

            #some descriptions have ))))), this removes them
            line["Text"] = line["Text"].replace(")", "").strip()

            #create transaction objects for each line
            new_trans = Transaction(
                category = line["Category"], 
                date = line["Date"], 
                amount = line["Amount"], 
                desc = line["Text"], 
                is_income = line["is_income"]
            )
            output_rows.append(new_trans)
    with open(output, mode = "w", encoding = "utf-8", newline = "") as f_out:
        fieldnames = ["category", "date", "amount", "desc", "is_income"]
        writer = csv.DictWriter(f_out, fieldnames = fieldnames)
        writer.writeheader()
        for trans in output_rows:
            writer.writerow({
                "category": trans.category,
                "date": trans.date.strftime("%Y-%m-%d"),
                "amount": trans.amount,
                "desc": trans.desc,
                "is_income": trans.is_income
            })  
        return output_rows