def removeUnwantedRows(fin):
    #removes student loans, internal transfers, etc.
    #these transactions do not represent an actual loss of personal wealth,
    #rather a transition between accounts out of the scope of this tracker
    #personal code to remove loan payments
    fin.transactions = [
        trans for trans in fin.transactions
        if not(
            trans.desc == "24085844276" 
            or trans.desc == "TrueLayer" 
            or "ATM" in trans.desc
            or "mum" in trans.desc.lower()
            or "transfer" in trans.desc.lower()
            or "account" in trans.desc.lower()
            or "savings" in trans.desc.lower()
            or "loan" in trans.desc.lower()
        )
    ]
    return fin.transactions
