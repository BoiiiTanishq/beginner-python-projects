import random


target = random.randint(1,100)
while True:
    try:
        guess = int(input("guess the number(1,100): "))
        if guess > target:
            print("too high")
        elif guess < target:
            print("too low")
        else:
            print("u guessed it")
            break
    except ValueError:
        print("enter a vald number: ")     
