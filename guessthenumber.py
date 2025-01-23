#Guess the number game!

import random


start = 1
end = 100

og_number = random.randint(start,end)
print(f"Select the number between {start} and {end}")

guesses = 0

is_guessed = True

while is_guessed:
    number = input("Enter the number: ")
    if number.isdigit():
        number = int(number)
        guesses +=1
        if number > end or number < start:
            print("Out of range!")
            print(f"Please enter from the number between {start} and {end}")
        elif number>og_number:
            print("HOT!")
        elif number<og_number:
            print("Cold")
        else:
            print("Correct!! You found it!")
            print("_______________________")
            print(f"Your total number of guess:{guesses}")
            print("_______________________")
            is_guessed = False
    else:
        print(f"Please enter from the number between {start} and {end}")