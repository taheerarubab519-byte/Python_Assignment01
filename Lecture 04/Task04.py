import random
secret_number = random.randint(1, 10)
while True:
    guess = int(input("Please enter a number between 1 and 10: "))
    if guess > secret_number:
        print("You guessed too high.")
    elif guess < secret_number:
        print("You guessed too low.")
    elif guess == secret_number:
        print("You guessed correctly.")
    else:
        print("You guessed incorrectly.")
        break