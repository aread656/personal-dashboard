import uuid
from datetime import datetime
from finance import Finance
class Transaction:
    #initialise a transaction
    def __init__(self,amount,category,date,description,type):
        self.id:str = str(uuid.uuid4().hex[:8]) 
        self.type = self.setType(type)
        self.amount:float = self.setAmount(amount)
        self.category:str = self.setCategory(category)
        self.date:str = self.setDate(date)
        self.description:str = description
        return
    
    def __str__(self): #string representation of a Transaction
        type_str = "Income" if self.type else "Expense"
        return f"{self.id} | {self.date} | {type_str} | {self.category} | {self.amount} | {self.description}"
    
    def setAmount(self,amount:float): #set a new amount
        try:
            #enforce that amount is a float
            self.amount = abs(float(amount))
        except ValueError:
            raise ValueError("Amount must be a valid number")
    def setCategory(self,category:str): #set a new category
        category = str(category).strip().capitalize()
        allowed = Finance.income_categories if self.type else Finance.expense_categories
        if category not in allowed:
            raise ValueError("Invalid category")
        self.category = category
    def setDate(self,date:str | datetime.date | datetime): #set a new date   
        if isinstance(date, str):
            try:
                parsed = datetime.strptime(date, "%Y-%m-%d")
                self.date = parsed.strftime("%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect date string format, expected YYYY-MM-DD")
        elif isinstance(date,(datetime,datetime.date)):
            self.date = date.strftime("%Y-%m-%d")
        else:
            raise TypeError("Date must be a string or datetime object")
    def setDescription(self,desc:str): #set a new description
        self.description = str(desc).strip()
    def setType(self,is_income:bool): #set the new type
        self.type = bool(is_income)

    def getDescription(self):
        return self.description
    def getDate(self):
        return self.date
    def getCategory(self):
        return self.category
    def getAmount(self):
        return self.amount
    def getType(self):
        return "Income" if self.type else "Expense"
#initialise a new transaction object, validating the input