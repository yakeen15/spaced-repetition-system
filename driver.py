from lib.Task import Task
import json

t = Task("401001",6,"2023-12-30")
t.testPrint()
t.upDate()
t.testPrint()
with open('output.json', 'w') as json_file:
    json.dump(t.getData(), json_file)