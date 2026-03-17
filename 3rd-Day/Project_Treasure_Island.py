print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': \n")
if direction == "left":
    inlake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.: \n")
    if inlake == "wait":
        door_color= input("You arrive at the island unharmed. There is a house with 3 doors. one re, one yellow and blue. wich colour do you choose?: \n")
        if door_color == "yellow":
            print("You win")
        else: print("Game over")
    else: print("Game over")
else:
    print("Game over")