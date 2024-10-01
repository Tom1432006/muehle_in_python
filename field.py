class bcolors:
    EMPTY = '\033[1;30m'
    PLAYER1 = '\033[33m'
    PLAYER2 = '\033[36m'
    ENDC = '\033[0m'

class Field:
    field_index = 0

    player_symbols = []

    # List to store all the connections with other fields
    connections = []

    # stores the piece, that lays on the board
    hold_piece = 0

    def __init__(self, field_index, player_symbols):
        self.field_index = field_index
        self.hold_piece = player_symbols[0]
        self.player_symbols = player_symbols

    def connect(self, field_to_connect):
        self.connections.append(field_to_connect)

    def change_hold_piece(self, new_piece):
        self.hold_piece = new_piece

    def hold_str(self):
        if self.hold_piece == self.player_symbols[0]:
            return bcolors.EMPTY + str(self.hold_piece) + bcolors.ENDC
        if self.hold_piece == self.player_symbols[1]:
            return bcolors.PLAYER1 + str(self.hold_piece) + bcolors.ENDC
        if self.hold_piece == self.player_symbols[2]:
            return bcolors.PLAYER2 + str(self.hold_piece) + bcolors.ENDC
        return str(self.hold_piece)
    