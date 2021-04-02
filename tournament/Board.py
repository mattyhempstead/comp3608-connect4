#import numpy as np

class Board:
    def __init__(self, state):
        self.state = state
        
        self.red_count = 0
        self.yellow_count = 0


        # Number in a row for each colour
        self.red_in_a_row = [0]*6
        self.yellow_in_a_row = [0]*6

        
        # Pieces in each column
        self.column_count = [0]*7


        self.grid = [[[0]*9 for i in range(7)] for j in range(6)]
        #self.grid = np.array(self.grid)

        pre_grid = [list(row) for row in state.split(",")]
        for r in range(6):
            for c in range(7):
                piece = pre_grid[r][c]
                if piece == "r":
                    self.place(1,r,c)
                elif piece == "y":
                    self.place(-1,r,c)

        # Array structure goes
        # Piece LL RR TT BB BL TR TL BR

        #print("INIT FINISHED")


    def __str__(self):
        s = ""
        for row in reversed(self.grid):
            for col in row:
                s += f" {col[0]: }"
                s += "["+"".join(map(str,col[1:]))+"]"
            s += "\n"
        #s += '='*23

        s += f'\nR: {self.red_count} {self.red_in_a_row}'
        s += f'\nY: {self.yellow_count} {self.yellow_in_a_row}'
        s += f'\n{self.column_count}'
        s += f'\n{self.eval()}'
        s += '\n'

        return s


    def place(self, piece, r, c):
        #print(f"Placing: {piece: } ({r},{c})")
        
        cell = self.grid[r][c]
        cell[0] = piece

        if piece == 1:
            self.red_count += 1
        else:
            self.yellow_count += 1

        self.column_count[c] += 1

        
        # Only need to check at most 3 in each direction
        # When traversing a line, if the line increases from 2 to 3, I know I
        # have one less 2-in-a-row and one more 3-in-a-row.
        # Same with when I remove a piece.


        # Sum left and right line to get horizontal length
        # Then update all piece in left and right line

        # Left line length
        LL = 1
        if c > 0 and self.grid[r][c-1][0] == piece: 
            LL += self.grid[r][c-1][1]

        # Right line length
        RR = 1
        if c < 6 and self.grid[r][c+1][0] == piece: 
            RR += self.grid[r][c+1][2]

        # Scan Left and update RR
        for i in range(LL):
            self.grid[r][c-i][2] = RR+i

        # Scan Right and update LL
        for i in range(RR):
            self.grid[r][c+i][1] = LL+i



        # Bottom line length
        BB = 1
        if r > 0 and self.grid[r-1][c][0] == piece: 
            BB += self.grid[r-1][c][3]

        # Top line length
        TT = 1
        if r < 5 and self.grid[r+1][c][0] == piece: 
            TT += self.grid[r+1][c][4]

        # Scan Bottom and update TT
        for i in range(BB):
            self.grid[r-i][c][4] = TT+i

        # Scan Top and update BB
        for i in range(TT):
            self.grid[r+i][c][3] = BB+i



        # BottomLeft line length
        BL = 1
        if r > 0 and c > 0 and self.grid[r-1][c-1][0] == piece: 
            BL += self.grid[r-1][c-1][5]

        # TopRight line length
        TR = 1
        if r < 5 and c < 6 and self.grid[r+1][c+1][0] == piece: 
            TR += self.grid[r+1][c+1][6]

        # Scan BottomLeft and update TR
        for i in range(BL):
            self.grid[r-i][c-i][6] = TR+i

        # Scan TopRight and update BL
        for i in range(TR):
            self.grid[r+i][c+i][5] = BL+i



        # TopLeft line length
        TL = 1
        if r < 5 and c > 0 and self.grid[r+1][c-1][0] == piece: 
            TL += self.grid[r+1][c-1][7]

        # BottomRight line length
        BR = 1
        if r > 0 and c < 6 and self.grid[r-1][c+1][0] == piece: 
            BR += self.grid[r-1][c+1][8]

        # Scan TopLeft and update BR
        for i in range(TL):
            self.grid[r+i][c-i][8] = BR+i

        # Scan BottomRight and update TL
        for i in range(BR):
            self.grid[r-i][c+i][7] = TL+i



        ## Count n-in-a-rows

        # n-in-a-row from Left to Right
        LLRR = LL + RR - 1
        if LLRR > 1:
            if piece == 1:
                if LL > 2:
                    self.red_in_a_row[LL-1 -2] -= 1
                    #print("Red lost", LL-1)
                if RR > 2:
                    self.red_in_a_row[RR-1 -2] -= 1
                    #print("Red lost", RR-1)
                self.red_in_a_row[LLRR -2] += 1
                #print("Red gained", LLRR)
            else:
                if LL > 2:
                    self.yellow_in_a_row[LL-1 -2] -= 1
                    #print("Yellow lost", LL-1)
                if RR > 2:
                    self.yellow_in_a_row[RR-1 -2] -= 1       
                    #print("Yellow lost", RR-1)
                self.yellow_in_a_row[LLRR -2] += 1
                #print("Yellow gained", LLRR)


        # n-in-a-row from Bottom to Top
        BBTT = BB + TT - 1
        if BBTT > 1:
            if piece == 1:
                if BB > 2:
                    self.red_in_a_row[BB-1 -2] -= 1
                    #print("Red lost", BB-1)
                if TT > 2:
                    self.red_in_a_row[TT-1 -2] -= 1
                    #print("Red lost", TT-1)
                self.red_in_a_row[BBTT -2] += 1
                #print("Red gained", BBTT)
            else:
                if BB > 2:
                    self.yellow_in_a_row[BB-1 -2] -= 1
                    #print("Yellow lost", BB-1)
                if TT > 2:
                    self.yellow_in_a_row[TT-1 -2] -= 1       
                    #print("Yellow lost", TT-1)
                self.yellow_in_a_row[BBTT-2] += 1
                #print("Yellow gained", BBTT)


        # n-in-a-row from BottomLeft to TopRight
        BLTR = BL + TR - 1
        if BLTR > 1:
            if piece == 1:
                if BL > 2:
                    self.red_in_a_row[BL-1 -2] -= 1
                    #print("Red lost", BL-1)
                if TR > 2:
                    self.red_in_a_row[TR-1 -2] -= 1
                    #print("Red lost", TR-1)
                self.red_in_a_row[BLTR -2] += 1
                #print("Red gained", BLTR)
            else:
                if BL > 2:
                    self.yellow_in_a_row[BL-1 -2] -= 1
                    #print("Yellow lost", BL-1)
                if TR > 2:
                    self.yellow_in_a_row[TR-1 -2] -= 1       
                    #print("Yellow lost", TR-1)
                self.yellow_in_a_row[BLTR -2] += 1
                #print("Yellow gained", BLTR)


        # n-in-a-row from TopLeft to BottomRight
        TLBR = TL + BR - 1
        if TLBR > 1:
            if piece == 1:
                if TL > 2:
                    self.red_in_a_row[TL-1 -2] -= 1
                    #print("Red lost", TL-1)
                if BR > 2:
                    self.red_in_a_row[BR-1 -2] -= 1
                    #print("Red lost", BR-1)
                self.red_in_a_row[TLBR -2] += 1
                #print("Red gained", TLBR)
            else:
                if TL > 2:
                    self.yellow_in_a_row[TL-1 -2] -= 1
                    #print("Yellow lost", TL-1)
                if BR > 2:
                    self.yellow_in_a_row[BR-1 -2] -= 1       
                    #print("Yellow lost", BR-1)
                self.yellow_in_a_row[TLBR -2] += 1
                #print("Yellow gained", TLBR)



    def remove(self, r, c):
        #print(f"Removing: ({r},{c})")

        cell = self.grid[r][c]
        piece = cell[0]
        cell[0] = 0

        if piece == 1:
            self.red_count -= 1
        else:
            self.yellow_count -= 1

        self.column_count[c] -= 1


        LL = cell[1]
        RR = cell[2]
        BB = cell[3]
        TT = cell[4]
        BL = cell[5]
        TR = cell[6]
        TL = cell[7]
        BR = cell[8]

        # Remove lines
        if piece == 1:
            in_a_row = self.red_in_a_row
        else:
            in_a_row = self.yellow_in_a_row

        if LL+RR-1 > 1:
            in_a_row[LL+RR-1 -2] -= 1
        if BB+TT-1 > 1:
            in_a_row[BB+TT-1 -2] -= 1
        if BL+TR-1 > 1:
            in_a_row[BL+TR-1 -2] -= 1
        if TL+BR-1 > 1:
            in_a_row[TL+BR-1 -2] -= 1

        # Add new line
        if LL > 2:
            in_a_row[LL-1 -2] += 1
        if RR > 2:
            in_a_row[RR-1 -2] += 1
        if BB > 2:
            in_a_row[BB-1 -2] += 1
        if TT > 2:
            in_a_row[TT-1 -2] += 1
        if BL > 2:
            in_a_row[BL-1 -2] += 1
        if TR > 2:
            in_a_row[TR-1 -2] += 1
        if TL > 2:
            in_a_row[TL-1 -2] += 1
        if BR > 2:
            in_a_row[BR-1 -2] += 1


        # Scan Left and update Right
        for i in range(LL):
            self.grid[r][c-i][2] -= RR

        # Scan Right and update Left
        for i in range(RR):
            self.grid[r][c+i][1] -= LL

        # Scan Bottom and update Top
        for i in range(BB):
            self.grid[r-i][c][4] -= TT

        # Scan Top and update Bottom
        for i in range(TT):
            self.grid[r+i][c][3] -= BB

        # Scan BottomLeft and update TopRight
        for i in range(BL):
            self.grid[r-i][c-i][6] -= TR

        # Scan TopRight and update BottomLeft
        for i in range(TR):
            self.grid[r+i][c+i][5] -= BL

        # Scan TopLeft and update BottomRight
        for i in range(TL):
            self.grid[r+i][c-i][8] -= BR

        # Scan BottomRight and update TopLeft
        for i in range(BR):
            self.grid[r-i][c+i][7] -= TL



    def eval(self):
        total = 0

        if any(self.red_in_a_row[2:]):
            return 10000
        if any(self.yellow_in_a_row[2:]):
            return -10000
    
        total += self.red_count
        total += 10 * self.red_in_a_row[0]
        total += 100 * self.red_in_a_row[1]
        total += 1000 * self.red_in_a_row[2]


        total -= self.yellow_count
        total -= 10 * self.yellow_in_a_row[0]
        total -= 100 * self.yellow_in_a_row[1]
        total -= 1000 * self.yellow_in_a_row[2]


        return total


    def is_winner(self):
        if sum(self.red_in_a_row[2:]) > 0:
            return True
        if sum(self.yellow_in_a_row[2:]) > 0:
            return True
        return False


