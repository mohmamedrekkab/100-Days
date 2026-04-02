def greet():
    print("Hellow")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

def greet_with_name(name):
    print(f"Hallow {name}")
    print(f"How do you do {name} ?")
    print(f"Isn't the weather nice today {name}?")

greet_with_name("Mohamed")

def greet_with(name, location):
    print(f"Hallow {name}")
    print(f"What is it like in {location} ?")

greet_with("Mohamed","Hamburg")

def greet_with2(name, location):
    print(f"Hallow {name}")
    print(f"What is it like in {location} ?")

greet_with2(location="Hamburg",name="Mohamed")
