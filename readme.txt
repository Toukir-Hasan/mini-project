This is a class and function based program
Index.py is the main file to run. All the classes are imported in this file.

**************************************************************************************************************
                                    Database:
Four json files are used as a database.

employee_list.json- This file contains the 10 employees information.

There are 6 columns in this file and their names are -

Name- Name of the person
ID-serial number
Role-This is a unique id based on it the program will decide the role of the person. Such as
0-GM
1-Manager of Software
2-Manager of Hardware
3-5: Worker of Software
6-9: worker of Hardware
Dept- Department name
password- login password
count- Number of work assigned to this person

task_list.json-This file contains the tasks' information. There are 7 columns in this file-

Name- Name of the work
Work_id- Work of the id
dept- Which department will do the work
rol-This is a uniq id based on it the program will decide the role of the person.
assignedBy- Name of the person who will assign the work
Status- Status of the work
assignedto- Name of the assigned person.

permission.json- This is a permission database 3 columns are there
id- ids are coming from task.json list
dept- the department is also comes from task.json
permission- writen by manager.

notification.jason-This is for saving the message. There are two columns

message-with work id and time message will be stored.
dept-dept will be stored
************************************************************************************************************
                                Important information

In this project there are two departments one is software and other one is hardware.

Company structure: 1 GM, 1 software Manager, 3 software workers, 1 Hardware Manger, 4 hardware worker

There is a unique columns in employee_list.json that's name is role.
                    0-GM
                    1-Manager of Software
                    2-Manager of Hardware
                    3-5: Worker of Software
                    6-9: worker of Hardware

****************************************************************************************************************
                                How the program works

 Run the index file- it will ask "please select 0 for registration or 1 for login:"

 if 0 is pressed- registerEmployee() function is called and this function will call class Employee and will dump
 the data in employee_list.json

 if 1 is pressed- it will ask for
 please Enter Your Name:
 please Enter Your Password:

 After entering the name and pass it will search in the employee_list.json

 Based on result people will enter the portal
                                            GM
 When GM takes entry, he/she can do 0-for task assign,1-for task status,2-for unassigned task,3-Notification,4-permission

task assign- registerTask() function will be called and the function will call GM_taskassigner Class and data will be dumped in task_list.jason
task status- gm_taskreport.report()  function will be called.
unassigned task-registerTask() function will be called and the function will call GM_taskassigner Class and  data will be dumped in task_list.jason
Notification- Notification_viewer() class is called it will view the notifications'
permission-Permission() class is called

                                        Software Manager
0-for task assign, 1-for Unassigned Task,2-Notification,3-cancel or reassign

task assign-  Manager_taskassigner() class will be called
Unassigned Task- registerTask() function will be called
Notification-class Notification_viewer()  class will be called
reassign-Permission() will be called.
                                    Hardware Manager
0-for task assign, 1-for Unassigned Task,2-Notification,3-cancel or reassign

task assign-  Manager_taskassigner() class will be called
Unassigned Task- registerTask() function will be called
Notification-class Notification_viewer()  class will be called
reassign-Permission() will be called.

                                    Worker Software

assign task to yourself? 0: yes, 1:No

yes-Workers_taskassigner() class will be called
No-It will take the person to login portal

                                    Worker Hardware

assign task to yourself? 0: yes, 1:No

yes-Workers_taskassigner() class will be called
No-It will take the person to login portal







