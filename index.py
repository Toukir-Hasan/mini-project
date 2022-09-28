import employee
import task
import json
import gm_taskassign
import gm_taskreport
import manager_taskassign
import worker_assigntask
import notificationpy


def registerEmployee():
    print("you are on the Registration Portal---")
    name = input("enter the name of the employee: ")
    id = input("enter the id of the employee: ")
    role = input("enter the role of the employee: ")
    dept = input("enter the dept of the employee: ")
    password = input("enter the password employee: ")
    count=int(0)

    employee.createEmployee(name, id, role, dept, password,count)


def registerTask():
    assignedBy=""
    rol=""

    print("You are in the Task Assign Portal----")
    name = input("enter the name of the Task: ")
    id = input("enter the work id of the Task: ")
    dept = input("enter the name of the dept: ")
    print("status: unassigned, assigned, cancel, reassign")
    status = input("enter the status of the Task: ") #unassigned, assigned, cancel, reassign
    if status=="assigned":
        print("rol:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H")
        role = input("enter the rol whome the task will be assigned: ")# role:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H
        rol=role
        result=gm_taskassign.checker(role)# this result is counting assigned task is 3 or less
        if(result):
            assignedBy = input("enter the name who is assigning the work: ")
            assignedTo=input("enter the name who will be doing the work: ")
            task.createTask(name, id, dept, rol, assignedBy, status,assignedTo)
            notificationpy.notification_gm_manager(id,dept,assignedTo)
    elif status=="unassigned":
        assignedTo=""
        assignedBy = input("enter the name who is assigning the work: ")
        task.createTask(name, id, dept, rol, assignedBy, status, assignedTo)









def login():
    role = "other"
    dept="other"
    name=input("please Enter Your Namme: ")
    password=input("please Enter Your Password: ")

    with open(employee.emp_list) as json_file:
        data = json.load(json_file)
    for i in data:
        if i["name"] == name and i["password"] == password:
            # print(i["name"])
            if i["role"] == "0":
                role = "GM"
                dept=i['dept']
                print("Welcome", i["name"], ",your role is", role, ",Department is: ", dept)
                wish=int(input("what you would like to do (0-for task assign,1-for task status,2-for unassigned task,3-Notification): "))
                if wish==0:
                    registerTask()
                elif wish==1:
                    gm_taskreport.report()
                elif wish == 2:
                    registerTask()
                elif wish == 3:
                    notificationpy.notification_gm_manager_viewer(i['role'])


            elif i["role"] == "1":
               role="M_software"
               dept = i['dept']
               print("Welcome", i["name"], ",your role is", role, ",Department is: ", dept)
               wish=int(input("what you would like to do (0-for task assign, 1-for Unassigned Task,2-Notification): "))
               if wish==0:
                   manager_taskassign.manager_taskassigner(dept)
               elif wish == 1:
                   registerTask()
               elif wish == 2:
                   notificationpy.notification_gm_manager_viewer(i['role'])




            elif i["role"] == "2":
                role = "M_hardware"
                dept = i['dept']
                print("Welcome", i["name"], ",your role is", role, ",Department is: ", dept)
                wish = int(input("what you would like to do (0-for task assign,1-for Unassigned Task,2-Notification): "))
                if wish == 0:
                    manager_taskassign.manager_taskassigner(dept)
                elif wish == 1:
                    registerTask()
                elif wish == 2:
                    notificationpy.notification_gm_manager_viewer(i['role'])

            elif i["role"] == "3" or i["role"] == "4" or i["role"] == "5"  :
                cha = "W_software"
                dept = i['dept']
                role=i['role']
                name=i['name']
                print("Welcome", i["name"], ",your role is", cha, ",Department is: ", dept)
                result=worker_assigntask.worker_self_task_assigner(dept,role,name)
            elif i["role"] == "6" or i["role"] == "7" or i["role"] == "8" or i["role"] == "9"  :
                role = "W_hardware"
                dept = i['dept']
                role = i['role']
                name = i['name']
                print("Welcome", i["name"], ",your role is", role, ",Department is: ", dept)
                result = worker_assigntask.worker_self_task_assigner(dept, role, name)

            break
    else:
        print("Wrong Name or Password. Please Try Again")


if __name__ == "__main__":
    while True:
        user_input = int(input("please select 0 for registration or 1 for login: "))
        if user_input==0:
            registerEmployee()
        elif (user_input==1):
            login()




# login("1122", "12345")
