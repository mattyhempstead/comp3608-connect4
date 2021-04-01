
class Board:
    def __init__(self, state):
        self.state = state
        
        self.red_count = 0
        self.yellow_count = 0


        # Number in a row for each colour
        self.red_in_a_row = [0]*6
        self.yellow_in_a_row = [0]*6


        self.grid = [[[0]*9 for i in range(7)] for j in range(6)]

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



    def __str__(self):
        s = ""
        for row in reversed(self.grid):
            for col in row:
                s += f" {col[0]: }"
                s += "["+"".join(map(str,col[1:]))+"]"
            s += "\n"
        s += '='*23

        s += f'\nR: {self.red_count}  -  Y: {self.yellow_count}' 
        s += f"\nR: {self.red_in_a_row}"
        s += f"\nY: {self.yellow_in_a_row}"

        return s


    def eval(self):
        total = 0
    
        total += self.red_count
        


        total -= self.yellow_count

        return total



    def place(self, piece, r, c):
        print(f"Placing: {piece: } ({r},{c})")
        
        cell = self.grid[r][c]
        cell[0] = piece

        if piece == 1:
            self.red_count += 1
        else:
            self.yellow_count += 1

        
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
            self.grid[r+i][c-i][5] = BL+i



        # TopLeft line length
        TL = 1
        if r > 0 and c > 0 and self.grid[r+1][c-1][0] == piece: 
            TL += self.grid[r+1][c-1][7]

        # BottomRight line length
        BR = 1
        if r < 5 and c < 6 and self.grid[r-1][c+1][0] == piece: 
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
                    print("Red lost", LL-1)
                if RR > 2:
                    self.red_in_a_row[RR-1 -2] -= 1
                    print("Red lost", RR-1)
                self.red_in_a_row[LLRR -2] += 1
                print("Red gained", LLRR)
            else:
                if LL > 2:
                    self.yellow_in_a_row[LL-1 -2] -= 1
                    print("Yellow lost", LL-1)
                if RR > 2:
                    self.yellow_in_a_row[RR-1 -2] -= 1       
                    print("Yellow lost", RR-1)
                self.yellow_in_a_row[LLRR -2] += 1
                print("Yellow gained", LLRR)


        # n-in-a-row from Bottom to Top
        BBTT = BB + TT - 1
        if BBTT > 1:
            if piece == 1:
                if BB > 2:
                    self.red_in_a_row[BB-1 -2] -= 1
                    print("Red lost", BB-1)
                if TT > 2:
                    self.red_in_a_row[TT-1 -2] -= 1
                    print("Red lost", TT-1)
                self.red_in_a_row[BBTT -2] += 1
                print("Red gained", BBTT)
            else:
                if BB > 2:
                    self.yellow_in_a_row[BB-1 -2] -= 1
                    print("Yellow lost", BB-1)
                if TT > 2:
                    self.yellow_in_a_row[TT-1 -2] -= 1       
                    print("Yellow lost", TT-1)
                self.yellow_in_a_row[BBTT-2] += 1
                print("Yellow gained", BBTT)


        # n-in-a-row from BottomLeft to TopRight
        BLTR = BL + TR - 1
        if BLTR > 1:
            if piece == 1:
                if BL > 2:
                    self.red_in_a_row[BL-1 -2] -= 1
                    print("Red lost", BL-1)
                if TR > 2:
                    self.red_in_a_row[TR-1 -2] -= 1
                    print("Red lost", TR-1)
                self.red_in_a_row[BLTR -2] += 1
                print("Red gained", BLTR)
            else:
                if BL > 2:
                    self.yellow_in_a_row[BL-1 -2] -= 1
                    print("Yellow lost", BL-1)
                if TR > 2:
                    self.yellow_in_a_row[TR-1 -2] -= 1       
                    print("Yellow lost", TR-1)
                self.yellow_in_a_row[BLTR -2] += 1
                print("Yellow gained", BLTR)


        # n-in-a-row from TopLeft to BottomRight
        TLBR = TL + BR - 1
        if TLBR > 1:
            if piece == 1:
                if TL > 2:
                    self.red_in_a_row[TL-1 -2] -= 1
                    print("Red lost", TL-1)
                if BR > 2:
                    self.red_in_a_row[BR-1 -2] -= 1
                    print("Red lost", BR-1)
                self.red_in_a_row[TLBR -2] += 1
                print("Red gained", TLBR)
            else:
                if TL > 2:
                    self.yellow_in_a_row[TL-1 -2] -= 1
                    print("Yellow lost", TL-1)
                if BR > 2:
                    self.yellow_in_a_row[BR-1 -2] -= 1       
                    print("Yellow lost", BR-1)
                self.yellow_in_a_row[TLBR -2] += 1
                print("Yellow gained", TLBR)




