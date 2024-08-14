
import sys


def print_field(field):
    print("\n -----------")
    print(f"| {field[1]} | {field[2]} | {field[3]} |")
    print("|---|---|---|")
    print(f"| {field[4]} | {field[5]} | {field[6]} |")
    print("|---|---|---|")
    print(f"| {field[7]} | {field[8]} | {field[9]} |")
    print(" -----------")


def player_move(current_player):
    try:
        return int(input(f"Player '{current_player}': Choose a field between 1-9: "))
    except ValueError:
        print("Error occurred. You have to restart the game.")
        sys.exit()


def check_move(move, field):
    if move <= 0 or move >= 10:
        print("Invalid input (no number between 1-9). Try again:")
        return False
    elif field[move] == "X" or field[move] == "O":
        print("Invalid input (field has already been selected). Try again:")
        return False
    else:
        return True


def draw_player_move(move, field, current_player):
    field[move] = current_player


def check_tie(field):
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and \
        field[4] != "4" and field[5] != "5" and field[6] != "6" and \
            field[7] != "7" and field[8] != "8" and field[9] != "9":
        return True


def check_win(field):
    # check rows
    if field[1] == field[2] == field[3]:
        return True
    elif field[4] == field[5] == field[6]:
        return True
    elif field[7] == field[8] == field[9]:
        return True

    # check columns
    elif field[1] == field[4] == field[7]:
        return True
    elif field[2] == field[5] == field[8]:
        return True
    elif field[3] == field[6] == field[9]:
        return True

    # check diagonals
    elif field[1] == field[5] == field[9]:
        return True
    elif field[3] == field[5] == field[7]:
        return True


def change_player(current_player):
    return "O" if current_player == "X" else "X"


def main():
    field = ["",
             "1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"
    running = True

    # game loop
    while running:
        # displaying field each iteration
        print_field(field)

        # player move logic (input, determining correct input, ...)
        move = player_move(current_player)
        is_correct_move = check_move(move, field)
        if is_correct_move:
            draw_player_move(move, field, current_player)
        else:
            continue

        # checking possible game endings
        is_tie = check_tie(field)
        if is_tie:
            print_field(field)
            print("Tie. Nobody won the game!")
            running = False

        is_winner = check_win(field)
        if is_winner:
            print_field(field)
            print(f"Player '{current_player}' won the game!")
            running = False

        # changing player for next iteration
        current_player = change_player(current_player)

    input("Press Button to end game.")
    sys.exit()


if __name__ == "__main__":
    main()
