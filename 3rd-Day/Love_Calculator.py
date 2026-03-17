print("The Love Calculator is calculating your score ...")
name1= input("What is your name?: ")
name2= input("What is their name?: ")
love_calculator=0
love=""
lover_names= (name1+name2).lower()
t= lover_names.count("t")
r= lover_names.count("r")
u= lover_names.count("u")
e= lover_names.count("e")

first_digit = t+r+u+e

l= lover_names.count("l")
o= lover_names.count("o")
v= lover_names.count("v")
e= lover_names.count("e")

second_digit = l+o+v+e

love_calculator= int(str(first_digit)+str(second_digit))
if love_calculator <10 and love_calculator> 90:
    love="You ge together like koke and mentos."
    print(f"Your score is: {love_calculator}, {love}")
elif love_calculator >= 40 and love_calculator <= 50:
    love="Yaou are alright together."
    print(f"Your score is: {love_calculator}, {love}")
else:
    print(f"Your score is: {love_calculator}.")