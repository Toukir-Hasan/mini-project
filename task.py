import json

task_list = "task_list.json"


class Task:
    def __init__(self, name, id, dept, rol, assignedBy, status):
        self.name = name
        self.id = id
        self.dept = dept
        self.rol = rol
        self.assignedBy = assignedBy
        self.status = status


def createTask(name, id, dept, rol,assignedBy,status):
    task = Task(name, id, dept, rol, assignedBy,status)
    with open(task_list) as json_file:
        data = json.load(json_file)

    data.append(
        {
            "name": task.name,
            "work_id": task.id,
            "dept": task.dept,
            "rol": task.rol,
            "assignedBy": task.assignedBy,
            "status": task.status
        }
    )
    with open(task_list, mode="w") as json_file:
        json.dump(data, json_file)
        print("Task Assigned!")
