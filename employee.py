import json

emp_list = "employee_list.json"


class Employee:
    def __init__(self, name, id, role, dept, password):
        self.name = name
        self.id = id
        self.role = role
        self.dept = dept
        self.password = password


def createEmployee(name, id, role, dept, password):
    emp = Employee(name, id, role, dept, password)
    with open(emp_list) as json_file:
        data = json.load(json_file)
    data.append(
        {
            "name": emp.name,
            "id": emp.id,
            "role": emp.role,
            "dept": emp.dept,
            "password": emp.password,
        }
    )
    with open(emp_list, mode="w") as json_file:
        json.dump(data, json_file)
        print("Employee Registered!")
