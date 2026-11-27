import random

number = random.randint(1,100)
attempts = 0

print("Hello! Guest!!")
print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter Your Guess Number:"))
    attempts += 1

    if guess < number:
        print("Too Low! Try Again.")
    elif guess > number:
        print("Too High! Try Again.")
    else:
        print(f"Congratulations! You are right in {attempts} attempts.")
        break

