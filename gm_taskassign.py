import json
emp_list="employee_list.json"
class GM_taskassigner:
    def __init__(self,role):
        self.role=role

    def checker_for_taskassign_by_GM(self):
        with open(emp_list) as json_file:
            data=json.load(json_file)

        for i in data:
            if i['role']==self.role:
                if i['count']==3:
                    print ("You Cannot assign task to this worker. This worker has already 3 assigned tasks")
                    return False
                    break
                else:
                    print(i['count'])
                    i['count']+=1
                    print()
                    with open(emp_list, mode="w") as json_file:
                        json.dump(data, json_file)
                    return True
                    break






def checker(role):
    a=GM_taskassigner(role)
    result=a.checker_for_taskassign_by_GM()
    return result



