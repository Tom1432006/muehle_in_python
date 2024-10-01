import game, os, random, player

not_done = True
turn = 0
pieces_left = 9
players = []
player_won = 0

""" Possible game states:
0 -> starting phase, players put down their pieces
1 -> second phase, players slider their pieces over the board
2 -> end game, player can jump
"""
game_state = 0
test = False # generate a random 0th phase, to test the second phase
game = game.Game()

def take_piece():
    game.print_board()
    isvalid = False
    while not isvalid:
        if test and game_state == 0: take = random.randint(0,23)
        else: take = input("Stein zum wegnehmen: ")
        isvalid = game.take_piece(int(take), players[turn], players[(turn+1)%2])

def initiate_players():
    os.system("cls")
    print("Spieleinstellungen: ")

    valid_checker = False
    while not valid_checker:
        name_p1 = input("Name Spieler 1: ")
        if name_p1.strip() != "":
            valid_checker = True
    
    valid_checker = False
    while not valid_checker:
        symbol_p1 = input("Symbol Spieler 1 (Enter für default): ")
        if len(symbol_p1) == 1 or symbol_p1 == "":
            valid_checker = True
        
    if symbol_p1 == "": symbol_p1 = "⬤"
    player1 = player.Player(0, name_p1, symbol_p1)

    os.system("cls")
    print("Spieleinstellungen: ")
    
    valid_checker = False
    while not valid_checker:
        name_p2 = input("Name Spieler 2: ")
        if name_p2.strip() != "":
            valid_checker = True
    
    valid_checker = False
    while not valid_checker:
        symbol_p2 = input("Symbol Spieler 2 (Enter für default): ")
        if len(symbol_p2) == 1 or symbol_p2 == "":
            valid_checker = True

    if symbol_p2 == "": symbol_p2 = "◯"
    player2 = player.Player(1, name_p2, symbol_p2)

    players.append(player1)
    players.append(player2)

if __name__ == "__main__":
    initiate_players()
    # game loop
    while not_done:
        os.system("cls")
        # print(f"Phase {game_state}")
        game.print_board()
        print(f"{players[turn].player_name} ist dran!")

        if game_state == 0:
            print(f"Du hast noch {players[turn].pieces_in_hand} Stein(e) übrig")
            valid_move = False
            while not valid_move:
                if test: move = random.randint(0,23)
                else:
                    move = input("Zug: ")
                    if move == "exit" or move == "000": 
                        exit()

                    try: int(move)
                    except: continue

                valid_move = game.turn_p0(int(move), players[turn])

            if game.check_muehle(int(move)):
                print(f"{players[turn].player_name} hat eine Mühle!")
                take_piece()

            turn = (turn+1) % 2 # alternate between 0 and 1

            # if all the nine pieces have been placed on the board, enter phase 1
            if players[1].pieces_in_hand == 0:
                game_state = 1
        elif game_state == 1:
            test = False
            valid_move = False
            while not valid_move:
                move = input("Zug: ")
                if move == "exit" or move == "000": 
                    exit()

                valid_move = game.turn_p1(move, players[turn])
            
            move_to = int(move.split(" ")[1])
            if game.check_muehle(move_to):
                print(f"{players[turn].player_name} hat eine Mühle!")
                take_piece()
                if players[(turn+1)%2].pieces_left_on_board == 2:
                    not_done = False
                    player_won = turn

            turn = (turn+1) % 2 # alternate between 0 and 1


    game.print_board()
    print(f"{players[player_won].player_name} hat gewonnen!")
