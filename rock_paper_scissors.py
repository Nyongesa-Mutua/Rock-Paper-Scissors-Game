import random
computer = 0
brain = 0

options = ["rock", "paper", "scissors"]
for i in range(1,6):
    b = random.choice(options)
    a = input("Enter Rock/Paper/Scissors/ q to quit    ").lower()
    if a == "q":
        quit()
    elif a not in options:
        continue
    else:
        print(b)
        if a==b:
            print("draw")
        elif a == "rock" and b == "paper":
            print("You lose")
            computer +=1
        elif a =="rock" and b == "scissors":
            print("You win")
            brain +=1
        elif a == "paper" and b == "scissors":
            print("You lose")
            computer +=1
        elif a == "paper" and b == "rock":
            print("You win")
            brain +=1
        elif a == "scissors" and b == "paper":
            print("You win")
            brain +=1
        elif a == "scissors" and b == "rock":
            print("You lose")
            computer +=1

print("computer:",computer)
print("Your score:", brain)
if computer>brain:
    print("Computer wins")
else:
    print("You win")
    
        
            
        