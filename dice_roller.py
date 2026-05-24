import random
dice=random.randint(1,6)
print("first roll:")
print(dice)
choice=input("Do you want to roll again? (yes/no): ")
while choice=="yes":
    dice=random.randint(1,6)
    print(dice)
    choice=input("Do you want to roll again? (yes/no): ")
    

print("goodbye")
