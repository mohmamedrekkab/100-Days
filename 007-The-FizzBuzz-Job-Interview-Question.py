for number in range(1,101):
    
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz, {number}/3 = {number/3}, {number}/5= {number/5}" )
    elif number %3 ==0 and number % 5 != 0:
        print(f"Fizz, {number}/3  = {number/3}")
    elif number %3 != 0 and number %5 ==0:
        print(f"Buzz, {number}/5  = {number/5}")
    else: print(number)