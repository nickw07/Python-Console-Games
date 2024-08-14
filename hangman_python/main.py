
import sys
import random
import hangman_additional_data


def get_random_word():
    return random.choice(hangman_additional_data.words).upper()


def display_hangman(fails):
    for line in hangman_additional_data.hangman_art[fails]:
        print(line)


def display_text(hint):
    for letter in hint:
        print(f"{letter}", end=" ")


def add_hint(guess, random_word, hint):
    for index, letter in enumerate(random_word):
        if letter == guess:
            hint[index] = guess


def check_guessed_letter(guess, guessed_letters):
    if guess in guessed_letters:
        print("Letter had been guessed already. \n")
        return True
    else:
        return False


def check_win(random_word, hint):
    if "".join(hint) == random_word:
        for letter in random_word:
            print(letter, end=" ")
        print("- You win!")
        return True
    else:
        return False


def check_lose(random_word, fails):
    if fails == 6:
        display_hangman(fails)
        print(f"You lose! - {random_word}")
        return True
    else:
        return False


def main():

    random_word = get_random_word()
    fails = 0
    hint = list("_" * len(random_word))
    guessed_letters = []
    running = True

    # game loop
    while running:

        # displaying each iteration
        display_hangman(fails)
        display_text(hint)

        # getting input
        guess = input("Guess a letter: ")
        guess = guess.upper()

        # determine correct input
        if not guess.isalpha() or len(guess) > 1:
            print("Invalid input. Try again. \n")
            continue

        # 1. correct guess
        if guess in random_word:

            # check if letter was guessed already
            if check_guessed_letter(guess, guessed_letters):
                continue

            else:
                print("Correct guess! \n")
                add_hint(guess, random_word, hint)
                guessed_letters.append(guess)

                if check_win(random_word, hint):
                    running = False

        # 2. wrong guess
        elif guess not in random_word:

            # check if letter was guessed already
            if check_guessed_letter(guess, guessed_letters):
                continue

            else:
                print("Wrong guess! \n")
                fails += 1
                guessed_letters.append(guess)

                if check_lose(random_word, fails):
                    running = False

    # loop was exited
    input("Press Button to end game: ")
    sys.exit()


if __name__ == "__main__":
    main()
