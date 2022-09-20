import json
task="task_list.json"
def report():
    with open(task) as json_file:
        data=json.load(json_file)

    for i in data:
        print(i)

