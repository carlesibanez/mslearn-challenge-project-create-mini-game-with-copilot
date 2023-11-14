import random

while True:
    # Start game
    user_in = input("Write 'rock', 'paper' or 'scissors' to play: ")
    assert user_in in ["rock", "paper", "scissors"], "Invalid input, try again"

    # Computer's turn
    computer_in = random.choice(["rock", "paper", "scissors"])

    if user_in == computer_in:
        print("It's a tie!")
    elif user_in == "rock":
        if computer_in == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif user_in == "paper":
        if computer_in == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user_in == "scissors":
        if computer_in == "rock":
            print("You lose!")
        else:
            print("You win!")

    # Ask for replay
    replay = input("Do you want to play again? (y/n) ")
    if replay == "n":
        break