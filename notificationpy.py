import datetime
import json
message="notification.json"
permission="permission.json"


class Notification:

    def __init__(self,id,dept,assignedto):
        self.id=id
        self.dept=dept
        self.assignedto=assignedto


    def queue_of_work(self):
        now = datetime.datetime.now()



        work= str("New Work ID "+self.id+" and department is "+self.dept+" assigned to "+self.assignedto+" Time "+now.strftime("%Y-%m-%d %H:%M:%S"))

        with open(message) as json_file:
            data = json.load(json_file)
        data.append(
            {
                "message": work,
                'dept':self.dept,

            }
        )

        with open(message, mode="w") as json_file:
            json.dump(data, json_file)
        #
        # if self.dept=="software":
        #     self.queue_of_work_ms.append(work)
        # elif self.dept=="hardware":
        #     self.queue_of_work_mh.append(work)





class Notification_viewer:
    def queue_of_work_view(self,role):

        if role=="0":
            with open(message) as json_file:
                data = json.load(json_file)
            for i in data:
                print(i)
        elif role=="1":
            with open(message) as json_file:
                data = json.load(json_file)
            for i in data:
                if i['dept']=='software':
                    print(i)
        elif role=="2":
            with open(message) as json_file:
                data = json.load(json_file)
            for i in data:
                if i['dept']=='hardware':
                    print(i)

class Permission():
    def __init__(self,id,dept,permission):
        self.id=id
        self.dept=dept
        self.permission=permission
    def message_for_permission(self):
        with open(permission) as json_file:
            data = json.load(json_file)
        data.append(
            {
                "id": self.id,
                'dept':self.dept,
                'permission':self.permission

            }
        )

        with open(permission, mode="w") as json_file:
            json.dump(data, json_file)




def notification_gm_manager(id,dept,assignedTo):

    info=Notification(id,dept,assignedTo)
    info.queue_of_work()

def notification_gm_manager_viewer(role):
    info=Notification_viewer()
    info.queue_of_work_view(role)


def permission_viewer(id,dept,permission):
    mes=Permission(id,dept,permission)
    mes.message_for_permission()
