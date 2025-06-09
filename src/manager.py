from financeTracker import finances
from guitarPractice import practices
from contactList import contacts

class Manager:
    def __init__(self):
        self.financeTracker = finances(100);
        self.guitarPractice = practices();
        self.contactList = contacts();
    def displayDashboard(self):
        return
    def test(self):
        print("Test for manager instance")