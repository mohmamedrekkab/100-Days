# Small Pizza (S): 15$
# Medium Pizza (M): 20$
# Large Pizza (L): 25$
# Add pepporoni for small Pizza (Y or N): 2$ 
# Add pepporoni for Medium or Large Pizza (Y or N): 3$
# Add extra chees for any Pizza (Y or N): 1$

print("Welcome to Python Pizza Deliveries!")
size = input("What size Pizza do you want? S, M or L: ")
add_pepporoni = input("Do you want pepporoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill =0

if size =="S":
    bill =15
    if add_pepporoni == "Y":
        bill +=2
elif size =="M":
    bill = 20
    if add_pepporoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepporoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Pizza size: {size}")
print(f"papporoni: {add_pepporoni}")
print(f"Extra cheese: {extra_cheese}")
print(f"your final Bill is: {bill}")
