print("Bill split calculator")

while True:
    print("\n1. Split a bill")
    print("2. Quit")
    
    choice = input("Choose (1 or 2): ")
    
    if choice == "2":
        print("Goodbye!")
        break
    
    if choice == "1":
        billamount = float(input("Enter the bill amount: "))
        tippercent = float(input("Enter the tip percentage: "))
        tipamount = (tippercent / 100) * billamount
        print(f"Tip amount = ${tipamount:.2f}")
        total = tipamount + billamount
        people = int(input("Enter the no. of people: "))
        amountper = total / people
        print(f"Each person pays ${amountper:.2f}")
    else:
        print("Invalid choice, enter 1 or 2")
