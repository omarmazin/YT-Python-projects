# paper,scissor,rock
import random
arr = ["paper","scissor","rock"]
randomChoice = random.choice(arr)
print(randomChoice)

inp = input("[1] = paper\n[2] = scissor\n[3] rock\n ")
if inp == "paper":
    if randomChoice == inp:
        print("You Win")
    else:
        print("You Lose")
    
if inp == "scissor":
    if randomChoice == inp:
        print("You Win")
    else:
        print("You Lose")

if inp == "rock":
    if randomChoice == inp:
        print("You Win")
    else:
        print("You Lose")