def greet_user(name):
    print("=========================================\n=========================================")
    print("          Project SERA v0.5")
    print("=========================================\n=======================================")
    print(f"Hello,{name}")
    print("I am SERA.\n Your personal Ai assistant")

def title():
     print("1.Study \n 2.Motivation \n 3.Information about me \n 4.organizer \n 5.Exit")

def study():
    print("Let's start learning.")
    print("1.Add Subjects")
    print("2.View Subjects")
    print("3.Remove Subjects")
    print("4.back")

def organizer():
    print("Let's organize your day.")
    print("1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.back")        
        


def motivation():
    print('KEEP LEARNING UNTIL "L" BECOMES SILENT')

def about_her():
    print("I am SERA.\n Your new personal Ai Assistant.\n i am still growing")    

def exit():
    print(f"goodbye,{name}\n See you soon. \n I am shutting down.")


subjects=[]    
def subj():
      for i in range(len(subjects)):
           print(i +1,subjects[i])

            
                   
# ======================================================================================       
# Name check
try :
    with open("memory.txt","r") as file:
        name=file.read()
        print("Welcome back,", name)
except FileNotFoundError:

        name=input("What is your name?")
        with open ("memory.txt","w")as file:
            file.write(name)
            print("nice to meet you.", name)       
# subject check
try:
    with open ("subjects.txt","r") as file:
        for subject in file.readlines():
            subjects.append(subject.strip())
except FileNotFoundError:
    with open ("subjects.txt","w") as file:
        pass



import json
from datetime import datetime
#  load tasks
try:
    with open("tasks.json","r") as file:
        tasks=json.load(file)
        # "take the string stored into due, covert it to datetime,and put back the converted value into due"
        for task in tasks:
            task["due"]=datetime.strptime(task["due"],"%Y-%m-%d %H:%M")
except FileNotFoundError:
    tasks=[]

# check reminders
# print("TASKS:",task)
for task in tasks:
    # print("DUE:", task["due"])
    # print("NOW:",datetime.now())
    if task["due"] <= datetime.now():
        print(" ⚠️ Task is due:",task["name"])

            
greet_user(name)
# main loop
main_running=True
while main_running:
 print("How can I help you today?")
 title()
 choice=int(input("enter your choice:"))
 if choice==1:
            # study loop
            study_running=True
            while study_running:
             study()
             choice1=int(input("enter your choice:"))
             if choice1==1:
                add=input("enter your subject:")
                subjects.append(add)
                with open ("subjects.txt","w") as file:
                    file.write("\n".join(subjects))
                print("your subject is added!!!!")      
                subj()            
              
             elif choice1==2:
              print("your subjects are:")
              subj()
              
             elif choice1==3:
              print("which subject do you want to remove?")
              subj()
              try:
                 remove=int(input("enter subject number:"))
              except ValueError:
                  print("please enter a valid subject number.")
                  continue
              if remove>=1 and remove<=len(subjects):
                  removed_subject=subjects[remove-1]
                  subjects.remove(removed_subject)
                  print(removed_subject, "is removed!!")
                  with open ("subjects.txt","w")as file:
                      file.write("\n".join(subjects))
              else:
                  print("enter a valid number")    

             elif choice1==4:
              study_running=False
              
              
             else:
              print("invalid choice!!\n please select between 1 to 4")
 elif choice==2:
      motivation()
 elif choice==3:
        about_her()
 elif choice==4:
    #    organizer_loop
       organizer_running=True
       while organizer_running:
        organizer()
        choice2=int(input("enter your choice:"))
        if choice2==1:
            task_name=input("enter you task:")
            task_date=input("enter the date (DD-MM-YYYY):")
            task_time=input("enter the time (HH:MM):")
            try:
                due=datetime.strptime(task_date + " " + task_time, "%d-%m-%Y %H:%M")
            except ValueError:
                print("Invalid date and time.")
                continue
            print(due)
            task={
                "name":task_name,
                "due":due
            }
            tasks.append(task)
            tasks_to_save=[]
            for task in tasks:
                tasks_to_save.append({"name":task["name"],"due": task["due"].strftime("%Y-%m-%d %H:%M")})
                with open("tasks.json","w")as file:
                    json.dump(tasks_to_save,file,indent=4)
            print("Task added succesfully!!")

        elif choice2==2:
            if len(tasks)==0:
                print("No task found.")
            else:
                for i in range(len(tasks)):
                    print(i+1, tasks[i]["name"],"-",tasks[i]["due"])    

        elif choice2==3:
            if len(tasks)==0:
                print("No tasks to remove.")
            else:
                for i in range(len(tasks)):
                    print(i+1, tasks[i]["name"])
            try:       
                remove=int(input("enter task number to remove:"))
            except:
                print("please enter a valid number of task.")
                continue
                if remove>=1 and remove<=len(tasks):
                 remove_task=tasks.pop(remove-1)
                tasks_to_save=[]
                for task in tasks:
                    tasks_to_save.append({"name":task["name"],"due":task["due"].strftime("%Y-%m-%d %H:%M")})
                with open ("tasks.json","w")as file:
                    json.dump(tasks_to_save, file, indent=4)
                print("Task removed:",remove_task["name"])   
            else:
                print("enter a valid number")    


        elif choice2==4:
            organizer_running=False
        else:
         print("invalid choice!!\n please select between 1 to 4")

            

 elif choice==5:
      main_running=False
 else:
        print("invalid choice!!\n please select between 1 to 4")


