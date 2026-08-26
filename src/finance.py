import os
import csv
from . import constants
from .transaction import Transaction
from .personalFunctions import removeUnwantedRows
from datetime import datetime
class Finance:
    def __init__(self, filename = "financeRecords.csv"):
        self.transactions = []
        self.filename = filename
    def readCSV(self,path):
        try:
            if path is None or isinstance(path,str) == False:
                raise TypeError("Error: Path must not be None")
            elif os.path.isdir(path):
                raise Exception("Error: Path must be to a file, not a directory")
            output_rows=[]
            if os.path.exists(path):
                with open(file=path,mode="r",encoding="cp1252",newline="") as f:
                    reader = csv.DictReader(f)
                    for line in reader:
                        #categorise -amount as expense, +amount as income
                        amt_str = line["Amount"].replace(",","").strip()
                        line["is_income"] = float(amt_str) > 0
                        line["Amount"] = abs(float(amt_str))

                        #use constants.py CATEGORY_MAP to map to custom categories
                        category_key = (line.get("Category"),line.get("Subcategory"))
                        mapped_category = constants.CATEGORY_MAP.get(category_key)
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
                            type = line["is_income"],
                            amount = line["Amount"], category = line["Category"],
                            date = line["Date"], description = line["Text"]
                        )
                        output_rows.append(new_trans)
                return output_rows
        except (Exception,TypeError) as e:
            print(f"Error: {e}")
            return None

    def addTransaction(self,type,amount,category,date,description):
        #create a new transaction instance
        #append to self.transactions
        #in try-except
        try:
            new = Transaction(
                type = type,
                amount = amount,
                category = category,
                date = date,
                description = description            
            )
            self.transactions.append(new)
            return new
        except (ValueError,TypeError) as e:
            print(f"Error when adding transaction: {e}")
            return None

    def deleteTransaction(self,id) -> Transaction | None:
        if (id is None) or (not isinstance(id,str)) or (id.lower() == "q"): return None
        for i,t in enumerate(self.transactions):
            if t.id == id:
                return self.transactions.pop(i)
        print(f"Transaction of id {id} not found")
        return None

    def getAllTransactions(self):
        return self.transactions

    def listTransactions(self):
        if self.transactions:
            for t in self.transactions:
                print(t)
            return
        print("No transactions recorded")
        return

    def clearAllTransactions(self):
        self.transactions.clear()

    def editTransaction(self,id,attribute,new_value) -> bool:
        #check through attributes
        #try-except block to protect against errors
        t = self.findTransaction(id)
        if not t:
            print(f"Transaction not found with {id}")
            return False
        try:    
            if (attribute == "type"): t.type = new_value
            elif (attribute == "amount"): t.amount = new_value
            elif (attribute == "category"): t.category = new_value
            elif (attribute == "date"): t.date = new_value
            elif (attribute == "description"): t.description = new_value
            else:
                print(f"Invalid attribute: {attribute}")
                return False
            print(f"Successfully edited transaction {id}")
            return True
        except(ValueError,TypeError) as e:
            print(f"Failed to edit: {e}")
            return False

    def findTransaction(self,id):
        if (id is None) or (not isinstance(id,str)) or (id.lower() == "q"): return None
        for t in self.transactions:
            if t.id == id:
                return t
        print(f"Transaction with id {id} not found")
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
