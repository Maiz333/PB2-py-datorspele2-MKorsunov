from time import sleep
from mymodule import *

GAME_OVER = False
game_field = []
row_num = 0
col_num = 0
speletaja_nr = 0

def initialize_game_field(size):
    global game_field
    game_field = [[" " for _ in range(size)] for _ in range(size)]

def chk_cell(row_num, col_num): 
    return game_field[row_num][col_num] == " "

def user_input(plr_num2):
    global row_num, col_num
    valid_input = False
    while not valid_input:
        print(f"Enter row and column numbers (0 to {SIZE_OF_FIELD - 1}):")
        row_num = int(input("Row: "))
        col_num = int(input("Column: "))
        print()
        if 0 <= row_num < SIZE_OF_FIELD and 0 <= col_num < SIZE_OF_FIELD:
            if chk_cell(row_num, col_num):
                valid_input = True
            else:
                print("Cell is already occupied. Try again.")
        else:
            print("Invalid input. Try again.")

def game_field_change(plr_num3): 
    if plr_num3 == 0:
        game_field[row_num][col_num] = "X"
    else:
        game_field[row_num][col_num] = "0"

def chk_winner(plr_num4): 
    global GAME_OVER
    if plr_num4 == 0:
        plr_sym = "X"
    else:
        plr_sym = "0"

    for i in range(SIZE_OF_FIELD):
        win = True
        for j in range(SIZE_OF_FIELD):
            if game_field[i][j] != plr_sym:
                win = False
                break
        if win:
            print("Player", plr_sym, "WIN")
            GAME_OVER = True
            return

    for i in range(SIZE_OF_FIELD):
        win = True
        for j in range(SIZE_OF_FIELD):
            if game_field[j][i] != plr_sym:
                win = False
                break
        if win:
            print("Player", plr_sym, "WIN")
            GAME_OVER = True
            return

    win = True
    for i in range(SIZE_OF_FIELD):
        if game_field[i][i] != plr_sym:
            win = False
            break
    if win:
        print("Player", plr_sym, "WIN")
        GAME_OVER = True
        return

    win = True
    for i in range(SIZE_OF_FIELD):
        if game_field[i][SIZE_OF_FIELD - 1 - i] != plr_sym:
            win = False
            break
    if win:
        print("Player", plr_sym, "WIN")
        GAME_OVER = True  

def show_field(size): 
    print()
    for row in range(size):
        for col in range(size):
            if game_field[row][col] == " ":
                print("5", end="")  
            else:
                print(game_field[row][col], end="")
        print()

def play_game(): 
    global speletaja_nr
    show_player_message(speletaja_nr % 2)
    user_input(speletaja_nr % 2)
    game_field_change(speletaja_nr % 2)
    show_field(SIZE_OF_FIELD)
    chk_winner(speletaja_nr % 2)
    speletaja_nr += 1

def main(args):
    global SIZE_OF_FIELD
    show_menu()
    choice = input("Enter your choice (1-3): ")
    while choice == "1":
        show_game_rules()
        sleep(5)
        print()
        show_menu()
        choice = input("Enter your choice (1-3): ")
    if choice == "2":
        SIZE_OF_FIELD = get_field_size() 
        initialize_game_field(SIZE_OF_FIELD)
        show_field(SIZE_OF_FIELD)
        while not GAME_OVER and speletaja_nr < SIZE_OF_FIELD * SIZE_OF_FIELD:
            play_game()
        if not GAME_OVER:
            print("It's a draw!")
            print("GAME OVER!!!")
    elif choice == "3":
        print("Exiting game. Goodbye!")
    else:
        print("Invalid choice. Exiting.")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
