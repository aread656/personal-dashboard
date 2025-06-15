from financeTracker import Finances
from guitarPractice import Practices
from contactList import Contacts

class Manager:
    def __init__(self):
        self.financeTracker = Finances(100);
        self.guitarPractice = Practices();
        self.contactList = Contacts();
    def displayDashboard(self):
        return
    def test(self):
        print("Test for manager instance")

