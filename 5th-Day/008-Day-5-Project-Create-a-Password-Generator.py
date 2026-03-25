import random

#First Methode

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
nbr_letters = int(input("How many letters would you like in your password?\n"))
nbr_numbers = int(input("How many numbers would you like in your password?\n"))
nbr_symbols = int(input("How many symbols would you like in your password?\n"))
password1 =""
for i in range(1, nbr_letters+1):
    password1+=random.choice(letters)

for i in range(1, nbr_numbers+1):
    password1+=random.choice(numbers)

for i in range (1, nbr_symbols+1):
    password1+=random.choice(symbols)
    

print(f"Your password from Metode 1 : {password1}")

# Second Methode
password_list=[]
for i in range(1, nbr_letters+1):
    password_list.append(random.choice(letters))

for i in range(1, nbr_numbers+1):
    password_list.append(random.choice(numbers))

for i in range (1, nbr_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password2=""
for char in password_list:
    password2 +=char
print(f"your Password from Metode 2 est: {password2}")