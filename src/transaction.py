import uuid
from datetime import datetime
from utils import INCOME_CATEGORIES,EXPENSE_CATEGORIES
class Transaction:
    #initialise a transaction
    def __init__(self,amount,category,date,description,type):
        self.id:str = str(uuid.uuid4().hex[:8]) 
        self.type = type
        self.amount:float = amount
        self.category:str = category
        self.date:str = date
        self.description:str = description
        return
    
    def __str__(self): #string representation of a Transaction
        type_str = "Income" if self.type else "Expense"
        return f"{self.id} | {self.date} | {type_str} | {self.category} | {self.amount} | {self.description}"

    #---------Type---------
    @property
    def type(self)->bool:
        return self._type
    @type.setter
    def type(self,is_income:bool): #set the new type, True for income & False for expense
        self._type = bool(is_income)

    #-----------Amount----------
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self,amount:float): #set a new amount
        try:
            #enforce that amount is a float
            self._amount = abs(float(amount))
        except ValueError:
            raise ValueError("Amount must be a valid number")

    #-----------Category----------
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,category:str): #set a new category
        category = str(category).strip().capitalize()
        from finance import Finance
        allowed = INCOME_CATEGORIES if self._type else EXPENSE_CATEGORIES
        if category not in allowed:
            raise ValueError("Invalid category")
        else:
            self._category = category

    #---------Date--------
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date:str | datetime.date | datetime): #set a new date   
        if isinstance(date, str):
            try:
                parsed = datetime.strptime(date, "%Y-%m-%d")
                self._date = parsed.strftime("%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect date string format, expected YYYY-MM-DD")
        elif isinstance(date,(datetime,datetime.date)):
            self._date = date.strftime("%Y-%m-%d")
        else:
            raise TypeError("Date must be a string or datetime object")
        
    #----------Description--------
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self,desc:str): #set a new description
        self._description = str(desc).strip()