import random
target_number = random.randint(0, 100)

max_attempts = 7
print('Welcome to the Guess the Number game!')
print("I've selected a number between 0 and 100. You have 10 attempts to guess it.")

for attempts in range(1, max_attempts + 1):
    guess = int(input("Guess the number: "))

    if guess == target_number:
        print("Congratulations! You guessed the correct number in", attempts, "attempt(s).")
    elif guess < target_number:
        print("The number is higher.")
    else:
        print("The number is lower.")