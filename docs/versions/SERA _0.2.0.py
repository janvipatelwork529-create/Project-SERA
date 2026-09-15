def greet_user(name):
    print("=========================================\n=========================================")
    print("          Project SERA v0.2")
    print("=========================================\n=======================================")
    print(f"Hello,{name}")
    print("I am SERA.\n Your personal Ai assistant")

def study():
    print("Let's start learning.")

def motivation():
    print('KEEP LEARNING UNTIL "L" BECOMES SILENT')

def about_her():
    print("I am SERA.\n Your new personal Ai Assistant.\n i am still growing")    

def exit():
    print(f"goodbye,{name}\n See you soon. \n I am shutting down.")

# ======================================================================================       

name=input("enter your name please:")
greet_user(name)
running=True
while running:
    print("How can I help you today?")
    print("1.Study \n 2.Motivation \n 3.Information about me \n 4.Exit")
    choice=int(input("enter your choice:"))


    if choice==1:
        study()
    elif choice==2:
        motivation()
    elif choice==3:
        about_her()
    elif choice==4:
        exit()
        running=False
    else:
        print("invalid choice!!\n please select between 1 to 4")

    if running:
         print("=========================================\n=========================================")
         print("Anything else")
         print("=========================================\n=======================================")
          




    




