class Player:
    pieces_in_hand = 9
    pieces_left_on_board = 0

    player_index = 0
    player_symbol = ""
    player_name = ""

    def __init__(self, index, name, symbol):
        self.player_index = index
        self.player_symbol = symbol
        self.player_name = name

    def take_piece(self):
        self.pieces_left_on_board -= 1
    
    def place_piece(self):
        self.pieces_in_hand -= 1
        self.pieces_left_on_board += 1