letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters2=[]

coding=input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
phrase=input("Type you message:\n").lower()


shiftnumber= int(input("Type the schift number:\n"))
if shiftnumber >26:
    shiftnumber = shiftnumber % 26
def encryption(p, n):
    phrase2=""
    if p=="encode":
        for n in range(n, 26+n):
            letters2.append(letters[n])
        #print(letters2)
        for i in range(len(phrase)):
            for j in range(26):
                if phrase[i] == letters[j]:
                #print(phrase[i])
                #print(letters2[j])
                    phrase2+=letters2[j]
            if phrase[i]==" ":
                phrase2+=" "
                #phrase2[i].replace=letters2[j]
        print(phrase2)
    
    elif p=="decode":
        for n in range(n, 27+n):
            letters2.append(letters[n])
    #print(letters2)
        for i in range(len(phrase)):
            for j in range(26):
                if phrase[i] == letters2[j]:
                #print(phrase[i])
                #print(letters2[j])
                    phrase2+=letters[j]
            if phrase[i]==" ":
                phrase2+=" "
                #phrase2[i].replace=letters2[j]        
    
        print(phrase2)

    
    #print(phrase2)    

encryption(coding, shiftnumber)
respons=input("Do you want to continue y / n: ")
if respons== "y":
    coding=input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    phrase=input("Type you message:\n").lower()
    encryption(coding, shiftnumber)




