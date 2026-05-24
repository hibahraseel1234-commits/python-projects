import random
secret_number=random.randint(1,20)
user_guess=0
attempts=0
while user_guess != secret_number:
    user_guess=int(input("guess a number: "))
    attempts+=1
    if user_guess > secret_number:
        print("too high!,try again")
    elif user_guess < secret_number:
        print("too low!try again")
print(attempts)        
print("yay you got it!")