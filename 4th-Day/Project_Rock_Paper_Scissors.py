import random

rock =''' Rock
     _______
----'    ___)
        (____)
        (_____)
        (______)
----.___(____)
'''


paper =''' Paper
     ______________
----'    __________)
        (___________)
        (_____________)
        (___________)
----.___(________)
'''

scissors =''' Scissor
     ______________
----'    __________)
        (___________)
        (_____________)
        (__)
----.___(_)
'''


game= [rock, paper, scissors]

computerchoice = random.randint(0, 2)
#print(computerchoice)
yourchoice = int(input("what do you Choose? Type 0 for Rock, 1 for Paper or 2 Scissors: \n"))
print(f"Computer chose: {game[computerchoice]}")
print(f"you chose: {game[yourchoice]}")
if yourchoice == 0 and computerchoice ==1:
    
    print("You lose")
if yourchoice == 0 and computerchoice ==2:
    
    print("You winn")
if  yourchoice == 1 and computerchoice ==0:
    print("You win")
if yourchoice == 1 and computerchoice ==2:
    print("You lose")
if yourchoice == 2 and computerchoice ==0:
    print("You lose")
if yourchoice == 2 and computerchoice ==1:
    print("You lose")
if yourchoice ==  computerchoice:
    print("You have the same choice with the computer")