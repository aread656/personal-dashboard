from src.transaction import Transaction
from src.constants import INCOME_CATEGORIES, EXPENSE_CATEGORIES
import pytest

#-------------Initialising---------------
def test_transaction_valid_init():
    t = Transaction(
        type=True, amount = 2.00, category = "Pay",
        date = "2026-01-01", description = "Week's Pay"
    )
    assert len(t.id) == 8
    assert t.type == True
    assert t.amount == 2.00
    assert t.category == "Pay"
    assert t.date == "2026-01-01"
    assert t.description == "Week's Pay"

#----------------IDs----------------------
def test_unique_ids():
    t1 = Transaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    t2 = Transaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t1.id != t2.id

#--------------Amount------------------
def test_valid_amount():
    t = Transaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t.amount == 2.00
def test_amount_zero():
    t = Transaction(True,0.00,"Pay","2026-01-01","Week's Pay")
    assert t.amount == 0
def test_amount_numeric_string():
    t = Transaction(True,"2.00","Pay","2026-01-01","Week's Pay")
    assert t.amount == 2.00
def test_amount_negative():
    t = Transaction(True,-2.00,"Pay","2026-01-01","Week's Pay")
    assert t.amount == 2.00
def test_amount_none():
    with pytest.raises(TypeError):
        Transaction(True,None,"Pay","2026-01-01","Week's Pay")
def test_amount_invalid():
    with pytest.raises(ValueError):
        Transaction(True,"None","Pay","2026-01-01","Week's Pay")

#----------------Type---------------------
def test_type_true():
    t = Transaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t.type == True
def test_type_false():
    t = Transaction(False,2.00,"Groceries","2026-01-01","Week's Pay")
    assert t.type == False
def test_type_none():
    with pytest.raises(TypeError):
        Transaction(None,2.00,"Groceries","2026-01-01","Week's Pay")
def test_type_invalid():
    with pytest.raises(TypeError):
            Transaction("None",2.00,"Groceries","2026-01-01","Week's Pay")

#--------------Category------------------------
def test_category_income_valid():
    t = Transaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t.category == "Pay"
def test_category_expense_valid():
    t = Transaction(False,2.00,"Groceries","2026-01-01","Week's Pay")
    assert t.category == "Groceries"
def test_category_expense_invalid():
    with pytest.raises(ValueError):
        Transaction(False,2.00,"Pay","2026-01-01","Week's Pay")
def test_category_income_invalid():
    with pytest.raises(ValueError):
        Transaction(True,2.00,"Groceries","2026-01-01","Week's Pay")
def test_category_none():
    with pytest.raises(ValueError):
        Transaction(True,2.00,None,"2026-01-01","Week's Pay")
def test_category_case_incorrect():
    t = Transaction(True,2.00,"pAy","2026-01-01","Week's Pay")
    assert t.category == "Pay"
def test_category_whitespace():
    t = Transaction(True,2.00,"       pay            ","2026-01-01","Week's Pay")
    assert t.category == "Pay"

#-------------------Date---------------------------
def test_date_valid():
    t = Transaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t.date == "2026-01-01"
def test_date_future():
    with pytest.raises(ValueError):
        Transaction(True,2.00,"Pay","2035-01-01","Week's Pay")
def test_date_impossible():
    with pytest.raises(ValueError):
        Transaction(True,2.00,"Pay","2026-02-29","Week's Pay")
def test_date_empty():
    with pytest.raises(ValueError):
        Transaction(True,2.00,"Pay","","Week's Pay")
def test_date_incorrect_type():
    with pytest.raises(TypeError):
        Transaction(True,2.00,"Pay",3026,"Week's Pay")
def test_date_none():
    with pytest.raises(TypeError):
        Transaction(True,2.00,"Pay",None,"Week's Pay")
def test_date_incorrect_separators():
    with pytest.raises(ValueError):
        Transaction(True,2.00,"Pay","3026/01/01","Week's Pay")
def test_date_wrong_format():
    with pytest.raises(ValueError):
        Transaction(True,2.00,"Pay","01-01-3026","Week's Pay")

#----------------------Description--------------
def test_desc_valid():
    t = Transaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t.description == "Week's Pay"
def test_desc_empty():
    t = Transaction(True,2.00,"Pay","2026-01-01","")
    assert t.description == ""
def test_desc_none():
    with pytest.raises(TypeError):
        Transaction(True,2.00,"Pay","2026-01-01",None)
def test_desc_incorrect_type():
    with pytest.raises(TypeError):
        Transaction(True,2.00,"Pay","2026-01-01",False)