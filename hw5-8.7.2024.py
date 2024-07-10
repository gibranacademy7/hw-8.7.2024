number: int = int(input("Insert an integer number: "));

if number % 5 == 0 and number % 3 == 0:
    print("Buzz Fizz")
elif number % 5 == 0:
    print("Fizz")
elif number % 3 == 0:
    print("Buzz")
else: print("The number is not divisible by 3 or 5")
