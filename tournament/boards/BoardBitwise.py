import numpy as np
import math
from functools import lru_cache, cache

FOURS = np.array([2113665, 270549120, 34630287360, 4227330, 541098240,
    69260574720, 8454660, 1082196480, 138521149440, 16909320, 2164392960,
    277042298880, 33818640, 4328785920, 554084597760, 67637280, 8657571840,
    1108169195520, 135274560, 17315143680, 2216338391040, 15, 1920, 245760,
    31457280, 4026531840, 515396075520, 30, 3840, 491520, 62914560, 8053063680,
    1030792151040, 60, 7680, 983040, 125829120, 16106127360, 2061584302080, 120,
    15360, 1966080, 251658240, 32212254720, 4123168604160, 16843009, 2155905152,
    275955859456, 33686018, 4311810304, 551911718912, 67372036, 8623620608,
    1103823437824, 134744072, 17247241216, 2207646875648, 2130440, 272696320,
    34905128960, 4260880, 545392640, 69810257920, 8521760, 1090785280,
    139620515840, 17043520, 2181570560, 279241031680])



class BoardBitwise:
    def __init__(self, state=",".join(["."*7]*7)):
        self.state = state
        #print(state)
        
        self.move_count = 0
        self.red_count = 0
        self.yellow_count = 0

        # Pieces in each column
        self.column_count = [0]*7



        self.pieces_r = 0
        self.pieces_y = 0

        i = 0
        for c in state:
            if c == ",": continue

            if c == "r":
                self.pieces_r |= 1 << i
                self.move_count += 1
                self.red_count += 1
                self.column_count[i%7] += 1
            if c == "y":
                self.pieces_y |= 1 << i
                self.move_count += 1
                self.yellow_count += 1
                self.column_count[i%7] += 1

            i += 1


        self.r_win = False
        self.y_win = False

        self.r_and = None
        self.y_and = None


        # Filter out the impossible FOURS for red and yellow
        #self.FOURS_r = FOURS[self.pieces_y & FOURS == 0]
        #self.FOURS_y = FOURS[self.pieces_r & FOURS == 0]
        #print(len(self.FOURS_r), len(self.FOURS_y))


    def generate_fours():
        fours = []

        # Vertical lines
        for c in range(7):
            for r in range(3):
                board = BoardBitwise()
                for i in range(4):
                    board.place(1, r+i, c)
                #print(board)
                #print(f"{board.pieces_r:042b}")
                fours.append(board.pieces_r)


        # Horizontal lines
        for c in range(4):
            for r in range(6):
                board = BoardBitwise()
                for i in range(4):
                    board.place(1, r, c+i)
                #print(board)
                #print(f"{board.pieces_r:042b}")
                fours.append(board.pieces_r)


        # BottomLeft to TopRight
        for c in range(4):
            for r in range(3):
                board = BoardBitwise()
                for i in range(4):
                    board.place(1, r+i, c+i)
                #print(board)
                #print(f"{board.pieces_r:042b}")
                fours.append(board.pieces_r)


        # TopLeft to BottomRight
        for c in range(4):
            for r in range(3,6):
                board = BoardBitwise()
                for i in range(4):
                    board.place(1, r-i, c+i)
                #print(board)
                #print(f"{board.pieces_r:042b}")
                fours.append(board.pieces_r)
       
        fours = np.array(fours)
        
        print(len(fours), fours)



    def __str__(self):
        s = ""
        
        row = ""
        for i in range(42):
            if (self.pieces_r >> i)%2 == 1:
                row += " r"
            elif (self.pieces_y >> i)%2 == 1:
                row += " y"
            else:
                row += " ."

            if i%7 == 6:
                s = row + "\n" + s
                row = ""


        s += f"R: {self.pieces_r:042b}\n"
        s += f"Y: {self.pieces_y:042b}\n"


        #for row in reversed(self.grid):
        #    for col in row:
        #        s += " " + ['o','.','x'][col[0]+1]
                #s += f" {col[0]: }"
                #s += "["+"".join(map(str,col[1:]))+"]"
        #    s += "\n"
        #s += '='*23

        s += f'\nR: {self.red_count}'
        s += f'\nY: {self.yellow_count}'
        s += f'\nCols: {self.column_count}'
        s += f'\nMoves: {self.move_count}'
        s += f'\nEval: {self.eval()}'
        s += '\n'

        return s

    
    def get_state_str(self):
        s = ""
        for row in self.grid:
            for col in row:
                if col[0] == 0:
                    s += "."
                elif col[0] == 1:
                    s += "r"
                elif col[0] == -1:
                    s += "y"
            s += ","
        s = s[:-1]

        return s



    def place(self, piece, r, c):
        #print(f"Placing: {piece: } ({r},{c})")
        self.move_count += 1
        self.column_count[c] += 1

        if piece == 1:
            self.pieces_r |= 1 << (c + r*7)
            self.red_count += 1

            self.r_win = self.get_r_win(self.pieces_r)
        else:
            self.pieces_y |= 1 << (c + r*7)
            self.yellow_count += 1

            self.y_win = self.get_y_win(self.pieces_y)


    
    def remove(self, piece, r, c):
        #print(f"Placing: {piece: } ({r},{c})")
        self.move_count -= 1
        self.column_count[c] -= 1

        if piece == 1:
            self.pieces_r &= ~(1 << (c + r*7))
            self.red_count -= 1

            self.r_win = False
        else:
            self.pieces_y &= ~(1 << (c + r*7))
            self.yellow_count -= 1

            self.y_win = False


    def skip(self):
        self.move_count += 1


    def eval(self):
        """
            Count number of 4-in-a-rows available.
            Subtract number for opponent.
        """

        if self.r_win:
            return +1000000
        elif self.y_win:
            return -1000000

        return 0


    @lru_cache(maxsize=4096)
    def get_r_win(self, pieces_r):
        # If quicker, can order by most likely to give 4-in-a-row
        #for line in FOURS:
        #    if self.pieces_r & line == line:
        #        return True
        #return False

        #self.r_and = self.pieces_r & FOURS
        #self.r_win = any(self.r_and == FOURS)
        #return self.r_win

        #return any(self.pieces_r & self.FOURS_r == self.FOURS_r)
        return any(self.pieces_r & FOURS == FOURS)


    @lru_cache(maxsize=4096)
    def get_y_win(self, pieces_y):
        # If quicker, can order by most likely to give 4-in-a-row
        #for line in FOURS:
        #    if self.pieces_y & line == line:
        #        return True
        #return False

        #self.y_and = self.pieces_y & FOURS
        #self.y_win = any(self.y_and == FOURS)
        #return self.y_win

        #return any(self.pieces_y & self.FOURS_y == self.FOURS_y)
        return any(self.pieces_y & FOURS == FOURS)


    def is_r_win(self):
        return self.r_win
    
    def is_y_win(self):
        return self.y_win


    def has_winner(self):
        return self.r_win or self.y_win



if __name__ == '__main__':

    #board = BoardBitwise('.ryyrry,.rryry.,..y.r..,..y....,.......,.......')
    #print(board)

    #board.place(1, 3, 6)
    #print(board)

    #board.remove(1, 3, 6)
    #print(board)


    print(FOURS)

    
    board = BoardBitwise()
    board.place(1, 0, 0)
    board.place(1, 0, 1)
    board.place(1, 0, 2)
    board.place(1, 0, 3)
    board.place(1, 3, 3)

    #board.place(-1, 1, 0)
    #board.place(-1, 1, 1)
    #board.place(-1, 1, 2)
    #board.place(-1, 1, 3)
    
    print(board)
    
    reds = board.pieces_r

    print(board.is_r_win())
    print(board.is_y_win())


    print(board.eval())


