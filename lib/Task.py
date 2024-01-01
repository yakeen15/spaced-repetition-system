import datetime
from lib.calc import getDate

class Task:
    def __init__(self, id_='', title='', diff=-1, date=None,dict_=None):
        if dict_ is not None:
            self.id = str(dict_['id'])
            self.title = str(dict_['title'])
            self.diff = int(dict_['diff'])
            self.date = datetime.datetime.strptime(dict_['due'], "%Y-%m-%d")
        else:
            self.id = id_
            self.title = title
            self.diff = diff
            if date is None:
                date = str(datetime.datetime.now())
            self.date = datetime.datetime.strptime(date, "%Y-%m-%d")

    def upDate(self):
        date = datetime.timedelta(days=getDate(self.diff))
        self.date = datetime.datetime.now() + date

    def testPrint(self):
        print(
            "ID: " + str(self.id) +
            "\nTask: " + self.title +
            "\nTo be done by: " + self.date.strftime("%Y-%m-%d") +
            "\nCurrent difficulty: " + str(self.diff)
        )

    def getData(self):
        data = {
            'id': self.id,
            'title': self.title,
            'diff': self.diff,
            'due': self.date.strftime("%Y-%m-%d")
        }
        return data
