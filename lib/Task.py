import datetime
from lib.calc import getDate

class Task:
    def __init__(self, id, diff, date=str(datetime.datetime.now())):
        self.id = id
        self.diff = diff
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
    def upDate(self):
        date = datetime.timedelta(days=getDate(self.diff))
        self.date = datetime.datetime.now() + date
    def testPrint(self):
        print("ID: "+str(self.id)+"\nTo be done by: "+self.date.strftime("%Y-%m-%d")+"\nCurrent difficulty: "+str(self.diff))
    def getData(self):
        dict = {'id': self.id, 'diff': self.diff, 'due': self.date.strftime("%Y-%m-%d")}
        return dict
