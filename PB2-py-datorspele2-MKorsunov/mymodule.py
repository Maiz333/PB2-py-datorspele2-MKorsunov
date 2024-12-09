player_name = ["player 1st", "player 2nd"]

def get_field_size():
    print()
    print("Izvēlieties Tic-Tac-Toe režģa izmēru:")
    print("1. 3x3")
    print("2. 4x4")
    print("3. 10x10")
    print("4. Pielāgots izmērs (min 3x3))")
    
    choice = input("Ievadiet savu izvēli(1-4): ")
    if choice == "1":
        return 3
    elif choice == "2":
        return 4
    elif choice == "3":
        return 10
    elif choice == "4":
        size = int(input("Ievadiet pielāgotu režģa izmēru (3 vai vairāk): "))
        if size < 3:
            print("Nederīgs izmērs. Pēc noklusējuma 3x3.")
            return 3
        return size
    else:
        print("Nederīga izvēle. Pēc noklusējuma 3x3.")
        return 3

def show_game_rules():
    print()
    print("Spēles noteikumi:")
    print("1. Spēle ir Tic-Tac-Toe ar pielāgojamu režģa izmēru.")
    print("2. 1 .spēlētājs spēlē ar X, bet 2. spēlētājs ar O.")
    print("3. Spēlētāji pārmaiņus liek savus simbolus uz režģa.")
    print("4. Mērķis ir izveidot simbolu rindu (horizontāli, vertikāli vai pa diagonāli) pirms pretinieka.")
    print("5. Ja visi lauciņi ir aizpildīti un neviens neuzvar, spēle beidzas ar neizšķirtu.")

def show_menu():
    print("Tic-Tac-Toe spēles izvēlne:")
    print("1. Rādīt spēles noteikumus")
    print("2. Sākt spēli")
    print("3. Iziet")
    
def show_player_message(plr_num):
    print()
    print(player_name[plr_num], "symbol: ", "X" if plr_num == 0 else "0")
