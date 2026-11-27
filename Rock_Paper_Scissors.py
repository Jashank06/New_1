import random

choices = ["Rock", "Paper", "Scissors"]
player_score = 0
Bot_score = 0

print("Welcome to Rock, Papers, Scissors !!")
print("Pick one Rock, Papers, Scissors.")

while True:
    player = input("Enter your Choice:")

    Bot = random.choice(choices)
    print(f"Bot Choose = {Bot}")

    if player == Bot:
        print("It's a tie! Great minds think alike.")

    elif (player == "Rock" and Bot == "Scissors"):
        print("You win! The bot is shaking right now.")
        player_score += 1

    elif (player == "Paper" and Bot == "Rock"):
        print("You win! The bot is shaking right now.")
        player_score += 1

    elif (player == "Scissors" and Bot == "Paper"):
        print("You win! The bot is shaking right now.")
        player_score += 1

    else:
        print("Beep boop! Bot wins. Better luck next time.")
        Bot_score += 1

    print(f"Score -> You:{player_score}, Bot_Score:{Bot_score}")