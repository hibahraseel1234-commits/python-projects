print("-- -CALCULATOR---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Enter your choice: ")
choice = int(input())
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: ")) 
if choice==1:
    print("result=",num1+num2)
elif choice==2:
    print("result=",num1-num2)
elif choice==3:
    print("result=",num1*num2)
elif choice==4:
    if num2!=0:
        print("result=",num1/num2)
    else:
        print("error")
else:
    print("invalid choice")
    
