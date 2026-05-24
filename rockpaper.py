import random
user_choice=input("rock, paper,scissors or quit")
userscore=0
compscore=0
while user_choice != "quit":
    comp_choice= random.choice (["rock","paper","scissors"])
    if (user_choice== "rock" and comp_choice =="scissors") or (user_choice=="paper" and comp_choice=="rock") or (user_choice=="scissors" and comp_choice=="paper"):
        print(comp_choice)
        print("you won this round")
        userscore= userscore+1
    elif (comp_choice== "rock" and user_choice =="scissors") or (comp_choice=="paper" and user_choice=="rock") or (comp_choice=="scissors" and user_choice=="paper"):
        print(comp_choice)
        print("you lost this round")
        compscore=compscore+1
    else:
        print("tie")
    user_choice=input("rock, paper,scissors or quit")
print(userscore)
print(compscore)
if userscore> compscore:
    print(" you won!")
else:
    print("you lose! better luck next time")
    
    