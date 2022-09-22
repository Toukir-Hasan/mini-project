import task
import gm_taskassign

class Manager_taskassigner:
    def __init__(self,dept):
        self.dept=dept
    def registration_task_software(self):
        assignedBy = ""
        rol = ""
        print("You are in the Task Assign Portal----")
        name = input("enter the name of the Task: ")
        id = input("enter the work id of the Task: ")
        dept = input("enter the name of the dept (software/hardware): ")
        if dept==self.dept:
            print("status: unassigned, assigned, cancel, resolve")
            status = input("enter the status of the Task: ")  # unassigned, assigned, pending, resolved
            if status == "assigned":
                print("rol:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H")
                role = input(
                    "enter the rol whom the task will be assigned (3-5:W): ")  # role:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H
                rol = role
                result = gm_taskassign.checker(role)  # this result is counting assigned task is 3 or less\
                #after assigning task a notification need to sent. notification module will be created here.
                if (result):
                    assignedBy = input("enter the name who is assigning the work: ")
                    assignedTo = input("enter the name who will be doing the work: ")
                    task.createTask(name, id, dept, rol, assignedBy, status, assignedTo)
            elif status=="Unassigned":
                assignedBy = input("enter the name who is assigning the work: ")
                assignedTo = ""
                task.createTask(name, id, dept, rol, assignedBy, status, assignedTo)


        else:
            print("you are Assigning task to Wrong Department!!")
            return False



    def registration_task_hardware(self):
        assignedBy = ""
        rol = ""
        print("You are in the Task Assign Portal----")
        name = input("enter the name of the Task: ")
        id = input("enter the work id of the Task: ")
        dept = input("enter the name of the dept (software/hardware): ")
        if dept==self.dept:
            print("status: unassigned, assigned, cancel, resolve")
            status = input("enter the status of the Task: ")  # unassigned, assigned, pending, resolved
            if status == "assigned":
                print("rol:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H")
                role = input(
                    "enter the rol whom the task will be assigned (6-9:W): ")  # role:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H
                rol = role
                result = gm_taskassign.checker(role)  # this result is counting assigned task is 3 or less\
                #after assigning task a notification need to sent. notification module will be created here.
                if (result):
                    assignedBy = input("enter the name who is assigning the work: ")
                    assignedTo = input("enter the name who will be doing the work: ")
                    task.createTask(name, id, dept, rol, assignedBy, status, assignedTo)

            elif status == "Unassigned":
                assignedBy = input("enter the name who is assigning the work: ")
                assignedTo = ""
                task.createTask(name, id, dept, rol, assignedBy, status, assignedTo)
        else:
            print("you are Assigning task to Wrong Department!!")
            return False









def manager_taskassigner(dept):
    a = Manager_taskassigner(dept)
    if dept=="software":
        a.registration_task_software()
    else:
        a.registration_task_hardware()


