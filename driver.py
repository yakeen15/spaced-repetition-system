from lib.Task import Task, Tasks
from lib.data import loadData, saveData, delData

t1 = Task("401001","Current electricity", 3, "2023-12-31")
t2 = Task("402001", "Static dynamics", 5, "2023-12-31")
list_dat = [t1, t2]
tasklist = Tasks(list_dat)
tasklist.delData(tasklist.findPos("401001"))
print(tasklist.contents())