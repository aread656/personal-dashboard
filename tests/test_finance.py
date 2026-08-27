from src.transaction import Transaction
from src.finance import Finance
import pytest
import os
import csv

@pytest.fixture
def fin():
    return Finance()
def sample_transactions():
    transactions = [(True,200.39,"Pay","2025-09-17","Part-time job"),
    (True,15.09,"Transfer","2026-06-18","Transfer"),
    (True,148.32,"Pay","2026-04-22","Part-time job"),
    (False,36.18,"Groceries","2025-12-16","Groceries"),
    (False,20.9,"Charity","2025-11-22","Foodbank.charity donation"),
    (False,18.29,"Clothing","2025-09-11","Clothing")]
    return [Transaction(*item) for item in transactions]
#---------------------------------------------------
#                   Adding Transactions
#---------------------------------------------------
def test_add_transaction_valid(fin):
    t = fin.addTransaction(True,2.00,"Pay","2026-01-01","Week's Pay")
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

#----------------------------------------------------------
#                       Deleting Transaction                
#----------------------------------------------------------
def test_delete_transaction_valid(fin):
    fin.transactions.extend(sample_transactions())
    initial_num_trans = len(fin.transactions)
    fin.deleteTransaction(fin.transactions[0].id)
    assert len(fin.transactions) == initial_num_trans - 1
def test_delete_transaction_invalid(fin):
    fin.transactions.extend(sample_transactions())
    assert fin.deleteTransaction("0") is None
def test_delete_transaction_none(fin):
    fin.transactions.extend(sample_transactions())
    assert fin.deleteTransaction(None) is None
def test_delete_transaction_quit_key(fin):
    fin.transactions.extend(sample_transactions())
    assert fin.deleteTransaction("q") is None
def test_delete_transaction_not_in_list(fin):
    t = Transaction(True,2.00,"Pay","2026-01-01","Example Transaction")
    assert fin.deleteTransaction(t.id) is None
def test_delete_transaction_id_wrong_type(fin):
    fin.transactions.extend(sample_transactions())
    assert fin.deleteTransaction(123) is None

#---------------------------------------------------------
#                 Getting All Transactions                
#---------------------------------------------------------
def test_get_all_transactions_non_empty_list(fin):
    fin.transactions.extend(sample_transactions())
    assert len(fin.getAllTransactions()) > 0
def test_get_all_transactions_empty_list(fin):
    assert len(fin.getAllTransactions()) == 0
#------------------------------------------------------------
#                 Clearing All Transactions                
#------------------------------------------------------------
def test_clear_all_transactions_non_empty_list(fin):
    fin.transactions.extend(sample_transactions())
    fin.clearAllTransactions()
    assert len(fin.transactions) == 0
def test_clear_all_transactions_non_empty_list(fin):
    fin.clearAllTransactions()
    assert len(fin.transactions) == 0
#-------------------------------------------------------------
#                       Find Transactions                       
#-------------------------------------------------------------
def test_find_transaction_id_exists(fin):
    fin.transactions.extend(sample_transactions())
    t = fin.findTransaction(fin.transactions[0].id)
def test_find_transaction_quit_key(fin):
    fin.transactions.extend(sample_transactions())
    assert fin.findTransaction("q") is None
def test_find_transaction_id_wrong_type(fin):
    fin.transactions.extend(sample_transactions())
    assert fin.findTransaction(123) is None
def test_find_transaction_id_not_exist(fin):
    fin.transactions.extend(sample_transactions())
    assert fin.findTransaction("w") is None
def test_find_transaction_empty_list(fin):
    fin.clearAllTransactions()
    t = fin.findTransaction("example_id")
    assert t is None