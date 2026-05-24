to_do=[]
print(" TO - DO")
choice=input("add , view, remove or exit ")
while choice!= "exit":
    if choice== "add":
        to_do.append(input("add task:"))
    elif choice=="view":
        print(to_do)
    elif choice=="remove":
        task=input("enter the task to be removed:")
        if task in to_do:
            to_do.remove(task)
        else:
            print("task not found")
    else:
        print("invalid choice")
    choice=input("add , view , remove or exit ")
print("goodbye!")    