import json
import notificationpy
task="task_list.json"
emp="employee_list.json"

class Workers_taskassigner:
    def __init__(self, dept,rol,name):
        self.dept=dept
        self.rol=rol
        self.name=name

    def assign_task_software(self):
        with open(task) as json_file:
            data=json.load(json_file)
        with open(emp) as json_file:
            data_1=json.load(json_file)

        for i in data:
            if i["status"]=="unassigned" and i['dept']==self.dept:
                print(i)

        wish=int(input("Do you like to assign task to yourself? 0: yes, 1:No  "))
        if wish==0:
            for i in data_1:
                if i['role']==self.rol:
                    if i['count']==3:
                        print("you cannot assign task to yourself because you have reached the max number of work")
                    else:
                        id_work = input("Please select the id of the work: ")
                        for i in data:
                            if i['work_id'] == id_work:
                                i['rol'] = self.rol
                                i['status'] = 'assigned'
                                i['assignedto'] = self.name
                                with open(task, mode="w") as json_file:
                                    json.dump(data, json_file)
                                notificationpy.notification_gm_manager(i['work_id'], i['dept'], i['assignedto'])
                                break
                        for i in data_1:
                            if i['role']==self.rol:
                                i['count']+=1
                                with open(emp, mode="w") as json_file:
                                    json.dump(data_1, json_file)
                                print("Task Assign to yourself")

                                return True
                                break
        else:
            return False
    def assign_task_hardware(self):
        with open(task) as json_file:
            data=json.load(json_file)
        with open(emp) as json_file:
            data_1=json.load(json_file)

        for i in data:
            if i["status"]=="unassigned" and i['dept']==self.dept:
                print(i)

        wish=int(input("Do you like to assign task to yourself? 0: yes, 1:No  "))
        if wish==0:
            for i in data_1:
                if i['role']==self.rol:
                    if i['count']==3:
                        print("you cannot assign task to yourself because you have reached the max number of work")
                    else:
                        id_work = input("Please select the id of the work: ")
                        for i in data:
                            if i['work_id'] == id_work:
                                i['rol'] = self.rol
                                i['status'] = 'assigned'
                                i['assignedto'] = self.name
                                with open(task, mode="w") as json_file:
                                    json.dump(data, json_file)
                                notificationpy.notification_gm_manager(i['work_id'],i['dept'],i['assignedto'])
                                break
                        for i in data_1:
                            if i['role']==self.rol:
                                i['count']+=1
                                with open(emp, mode="w") as json_file:
                                    json.dump(data_1, json_file)
                                print("Task Assign to yourself")
                                return True
                                break

        else:
            return False







def worker_self_task_assigner(dept,rol,name):
    a=Workers_taskassigner(dept,rol,name)

    if dept=="software":
        a.assign_task_software()
    else:
        a.assign_task_hardware()






