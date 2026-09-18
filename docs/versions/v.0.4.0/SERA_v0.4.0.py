def greet_user(name):
    print("=========================================\n=========================================")
    print("          Project SERA v0.3")
    print("=========================================\n=======================================")
    print(f"Hello,{name}")
    print("I am SERA.\n Your personal Ai assistant")

def title():
     print("1.Study \n 2.Motivation \n 3.Information about me \n 4.Exit")

def study():
    print("Let's start learning.")
    print("1.Add Subjects")
    print("2.View Subjects")
    print("3.Remove Subjects")
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

try :
    with open("memory.txt","r") as file:
        name=file.read()
        print("Welcome back,", name)
except FileNotFoundError:

        name=input("What is your name?")
        with open ("memory.txt","w")as file:
            file.write(name)
            print("nice to meet you.", name)       

try:
    with open ("subjects.txt","r") as file:
        for subject in file.readlines():
            subjects.append(subject.strip())
except FileNotFoundError:
    with open ("subjects.txt","w") as file:
        pass

            
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
              remove=int(input("enter subject number:"))
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
        main_running=False
 else:
        print("invalid choice!!\n please select between 1 to 4")


