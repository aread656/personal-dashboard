from src.transaction import Transaction
from src.finance import Finance
import pytest
import os
import csv

@pytest.fixture
def fin():
    return Finance()
#---------------------------------------------------
#                   Adding Transactions
#---------------------------------------------------
def test_add_transaction_valid(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    # assert unique ID
    for trans in fin.transactions:
        if (trans != t):
            assert trans.id != t.id
    # assert transaction successfully added
    assert t in fin.transactions
    # assert transaction details are correct
    for trans in fin.transactions:
        if (trans.id == t.id):
            assert t.type == True
            assert t.amount == 2.00
            assert t.category == "Pay"
            assert t.date == "2026-01-01"
            assert t.description == "Week's Pay"

#----------------Amount------------------
def test_add_transaction_amount_zero(fin):
    t = fin.addTransaction(True,0.00,"Pay","2026-01-01","Week's Pay")
    assert t.amount == 0
def test_add_transaction_amount_numeric_string(fin):
    t = fin.addTransaction(True,"2.00","Pay","2026-01-01","Week's Pay")
    for trans in fin.transactions:
        if (trans.id == t.id):
            assert t.amount == 2.00
def test_add_transaction_amount_negative(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    for trans in fin.transactions:
        if (trans.id == t.id):
            assert t.amount == 2.00
def test_add_transaction_amount_none(fin):
    t = fin.addTransaction(True,None,"Pay","2026-01-01","Week's Pay")
    assert t is None
    assert t not in fin.transactions
def test_add_transaction_amount_invalid(fin):
    t = fin.addTransaction(True,"None","Pay","2026-01-01","Week's Pay")
    assert t is None
    assert t not in fin.transactions

#------------------Type---------------
def test_add_transaction_type_true(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t.type == True
def test_add_transaction_type_false(fin):
    t = fin.addTransaction(False,2.00,"Bills","2026-01-01","Week's Bills")
    assert t.type == False
def test_add_transaction_type_none(fin):
    t = fin.addTransaction(None,2.00,"Pay","2026-01-01","Week's Pay")
    assert t is None
def test_add_transaction_type_invalid(fin):
    t = fin.addTransaction("True",2.00,"Pay","2026-01-01","Week's Pay")
    assert t is None

#----------------Category-----------------
def test_add_transaction_category_income_valid(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01","Week's Pay")
    assert t.category == "Pay"
def test_add_transaction_category_expense_valid(fin):
    t = fin.addTransaction(False,2.00,"Bills","2026-01-01","Week's Pay")
    assert t.category == "Bills"
def test_add_transaction_category_income_invalid(fin):
    t = fin.addTransaction(True,2.00,"Bills","2026-01-01","Week's Pay")
    assert t is None
def test_add_transaction_category_expense_invalid(fin):
    t = fin.addTransaction(False,2.00,"Pay","2026-01-01","Week's Pay")
    assert t is None
def test_add_transaction_category_none(fin):
    t = fin.addTransaction(True,2.00,None,"2026-01-01","Week's Pay")
    assert t is None
def test_add_transaction_category_case_incorrect(fin):
    t = fin.addTransaction(True,2.00,"pAY","2026-01-01","Week's Pay")
    assert t.category == "Pay"
def test_add_transaction_category_whitespace(fin):
    t = fin.addTransaction(True,2.00,"                   Pay          ","2026-01-01","Week's Pay")
    assert t.category == "Pay"

#----------------Date-----------------
def test_add_transaction_date_future(fin):
    t = fin.addTransaction(True,2.00,"Pay","2036-01-01","Week's Pay")
    assert t is None
def test_add_transaction_date_impossible(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-02-29","Week's Pay")
    assert t is None
def test_add_transaction_date_empty(fin):
    t = fin.addTransaction(True,2.00,"Pay","","Week's Pay")
    assert t is None
def test_add_transaction_date_incorrect_type(fin):
    t = fin.addTransaction(True,2.00,"Pay",20260101,"Week's Pay")
    assert t is None
def test_add_transaction_date_none(fin):
    t = fin.addTransaction(True,2.00,"Pay",None,"Week's Pay")
    assert t is None
def test_add_transaction_date_incorrect_separators(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026/01/01","Week's Pay")
    assert t is None
def test_add_transaction_date_wrong_format(fin):
    t = fin.addTransaction(True,2.00,"Pay","01-01-2026","Week's Pay")
    assert t is None

#------------------Description---------------
def test_add_transaction_desc_empty(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01","")
    assert t.description == ""
def test_add_transaction_desc_none(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01",None)
    assert t is None
def test_add_transaction_desc_incorrect_type(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01",123)
    assert t is None

#------------------------------------------------------------
#                       Reading CSV
#------------------------------------------------------------
def test_read_csv_valid_path(fin):
    path = "data/one_line_statement.csv"
    rows = fin.readCSV(path)
    assert len(rows) > 0