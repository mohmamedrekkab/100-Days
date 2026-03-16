print("Welcome to the tip calculator!")
total_bill= float(input("What was the total bill?: "))
percentage= float(input("What percentage would you like to give? :"))
people = float(input("How many people to split the bill?: "))

each_person= round(total_bill*(1+percentage/100)/people,2)
print(f"Each person should pay: {each_person}") 