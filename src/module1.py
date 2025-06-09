#manager class
class Manager:
    def init(self):
        self.finances = fTracker();
        self.guitar = gPractice();
        self.contacts = cList();
        return;

    def launchDashboard(self):
        #launches the dashboard menu, be it text or GUI
        return;

#financial tracker class
class fTracker:
    def init(self):
        return;
    def loadTransactions(self):
        #read a file of previous transactions
        return;
    def addTransaction(self):
        #add a new row to the file
        return;
    def weekPay(self):
        #this week's pay. will have a unique id which transactions will store
        #to allow for the tracking of remaining pay

#guitar practice class
class gPractice:
    def init(self):
        return;
    def displayRepertoire(self):
        #load and display the whole current repertoire
#contacts list class
class cList:
    def init(self):
        return;