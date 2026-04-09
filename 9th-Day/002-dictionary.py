programming_dictionary ={
"Bug":"An error in a program that prevents the program from running ",
"Function":" A piece of code that you can easily call over and over again",
"Loop":"The  action of doing something over and over agin."

}

print(programming_dictionary)
programming_dictionary["Condition"] = "Like 'if'"
print(programming_dictionary)

programming_dictionary ={}
print(f"The programming dictionary is: {programming_dictionary}")

programming_dictionary["Bug"] = "A month in your computer"
print(f"The programming dictionary is: {programming_dictionary}")

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])