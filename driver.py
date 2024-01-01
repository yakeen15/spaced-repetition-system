from lib.Task import Task
import json
from lib.data import loadData, saveData

t = []
t_data = []
for i in range(0,10):
    t.append(Task("40100"+str(i),"NNNigga",3,"2024-01-01"))
for task in t:
    t_data.append(task.getData())
saveData(t_data,'data/data.json')
tasks = loadData('data.json')
print(tasks)
for task in tasks:
    t = Task(dict_=task)
    t.testPrint()