import os
import csv
import utils
from transaction import Transaction
from personalFunctions import removeUnwantedRows
from datetime import datetime
class Finance:
    def __init__(self, filename = "financeRecords.csv"):
        self.transactions = []
        self.filename = filename
    def readCSV(self,path):
        output_rows=[]
        if os.path.exists(path):
            with open(file=path,mode="r",encoding="cp1252",newline="") as f:
                reader = csv.DictReader(f)
                for line in reader:
                    #categorise -amount as expense, +amount as income
                    amt_str = line["Amount"].replace(",","").strip()
                    line["is_income"] = float(amt_str) > 0
                    line["Amount"] = abs(float(amt_str))

                    #use utils CATEGORY_MAP to map to custom categories
                    category_key = (line.get("Category"),line.get("Subcategory"))
                    mapped_category = utils.CATEGORY_MAP.get(category_key)
                    if not mapped_category:
                        line["Category"]="Misc"
                    else:
                        line["Category"]=mapped_category

                    dt = datetime.strptime(line["Date"],"%m/%d/%Y")
                    line["Date"]=dt.strftime("%Y-%m-%d")

                    #remove unecessary rows
                    line.pop("Balance",None)
                    line.pop("Status",None)
                    line.pop("Reconciled",None)
                    line.pop("Subcategory",None)

                    new_trans = Transaction(
                        amount = line["Amount"], category = line["Category"],
                        date = line["Date"], description = line["Text"],
                        type = line["is_income"]
                    )
                    output_rows.append(new_trans)
        return output_rows

    def addTransaction(self,type,amount,category,date,desc):
        #create a new transaction instance
        #append to self.transactions
        #in try-except
        try:
            new = Transaction(
                amount = amount,
                category = category,
                date = date,
                description = desc,
                type = type
            )
            self.transactions.append(new)
        except (ValueError,TypeError) as e:
            print(f"Error when adding transaction: {e}")

    def deleteTransaction(self,id) -> Transaction:
        for i,t in enumerate(self.transactions):
            if t.id == id:
                return self.transactions.pop(i)
        return None

    def listTransactions(self):
        if self.transactions:
            for t in self.transactions:
                print(t)
            return
        print("No transactions recorded")
        return

    def editTransaction(self,id,attribute,new_value) -> bool:
        #check through attributes
        #try-except block to protect against errors
        t = self.findTransaction(id)
        if not t:
            print(f"Transaction not found with {id}")
            return False
        try:
            match(attribute):
                case "type":
                    t.type = new_value
                case "amount":
                    t.amount = new_value
                case "category":
                    t.category = new_value
                case "date":
                    t.date = new_value
                case "description":
                    t.description = new_value
                case _:
                    print(f"Invalid attribute: {attribute}")
                    return False
            print(f"Successfully edited transaction {id}")
            return True
        except(ValueError,TypeError) as e:
            print(f"Failed to edit: {e}")
            return False

    def findTransaction(self,id):
        for t in self.transactions:
            if t.id == id:
                return t
        return None

    def saveToCSV(self):
        with open(file = self.filename, mode = "w", encoding = "cp1252",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id","date","type","category","amount","description"])
            for t in self.transactions:
                writer.writerow([
                    t.id,t.date,
                    t.type,
                    t.category,t.amount,t.description
                ])
    
if __name__ == "__main__":
    f = Finance()
    f.transactions = f.readCSV("data/StatementJul25-Apr26.csv")
    f.transactions = removeUnwantedRows(f)
    f.listTransactions()
    f.saveToCSV()
