eventotal = 0

for number in range(0,101,2):
    print(number)
    eventotal+=number
print(eventotal)

#second Methode

somme =0
for chifre in range(1,101):
    if chifre % 2 == 0:
        print(f"chifre est: {chifre}")
        somme +=chifre
print(f"la somme est: {somme}")