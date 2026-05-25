expenses=[]
print("-----EXPENSE TRACKER-----")
def show_total(expense_list):
    total=sum(expense_list)
    print("total money spent: ", total)
menu=0

while menu!=4 :
    menu= int(input("1. add \n 2.view\n 3. total \n 4.quit \n choose and option(1-4):"))
    if menu==1:
        amount= float(input("enter the amount: "))
        expenses.append(amount)
    elif menu==2:
        print(expenses)
    elif menu==3:
        show_total(expenses)
    elif menu==4:
        print("processing exit....")
    else:
        print("invalid choice, please choose between (1-4)")
print ("goodbye")


