n= int(input("Give us the number that you wante to check it: "))

def prime_cheker(number):
    i=1
    b=False
    list_divided_number=[]
    while i<=number:
        if number % i==0 and i !=1 and i !=number:
            #print("That is no prime number")
            b=True
            list_divided_number.append(i)

        i+=1
    if b==False:
        print(f"{number}: That is a prime number")
    else: 
        print(f"{number}: This is not a prime number")
        print(f"and his list of divided number is: {list_divided_number}")
prime_cheker(n)

