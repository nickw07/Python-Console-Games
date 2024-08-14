
import sys
import random
import rps_additional_data


def get_computer_choice(options):
    return random.choice(options)


def display_input(computer_choice, user_choice):
    print(f"Computer chose: {computer_choice}")
    print(rps_additional_data.rps_art[computer_choice])

    print(f"You chose: {user_choice}")
    print(rps_additional_data.rps_art[user_choice])


def compare_input(computer_choice, user_choice):

    display_input(computer_choice, user_choice)

    # checking all possible inputs
    if computer_choice == user_choice:
        print("Tie! \n")

    elif computer_choice == "rock":
        if user_choice == "paper":
            print("You win! \n")
        elif user_choice == "scissors":
            print("You lose! \n")

    elif computer_choice == "paper":
        if user_choice == "scissors":
            print("You win! \n")
        if user_choice == "rock":
            print("You lose! \n")

    elif computer_choice == "scissors":
        if user_choice == "rock":
            print("You win! \n")
        if user_choice == "paper":
            print("You lose! \n")


def main():

    options = ["rock", "paper", "scissors"]
    running = True

    # game loop
    while running:

        # getting input
        computer_choice = get_computer_choice(options)
        user_choice = input("Rock, paper or scissors? ").lower()

        # determine correct input
        if user_choice.isalpha() and user_choice in options:
            compare_input(computer_choice, user_choice)
        else:
            print("Invalid input. Try again. \n")
            continue

        # check if player wants to play again
        if input("Play again (y/n): ").lower() != "y":
            running = False

    sys.exit()


if __name__ == '__main__':
    main()
