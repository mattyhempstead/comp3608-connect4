import numpy as np
import math
from functools import lru_cache, cache

from boards.BoardBitwise import BoardBitwise, FOURS


class BoardBitwiseLines(BoardBitwise):

    def eval(self):
        """
            Count number of 4-in-a-rows available.
            Subtract number for opponent.
        """

        #if self.r_win:
        if self.r_win:
            return +1000000
        #elif self.y_win:
        elif self.y_win:
            return -1000000


        # Check whether each 4-in-a-row exists for red
        # Bitwise & with yellow. Zero implies yellow has filled none of the
        # spots.

        #lines_r = sum(self.y_and == 0)
        #lines_r = sum(self.pieces_y & FOURS == 0)
        lines_r = self.get_lines_r(self.pieces_y)
        #print("R Left:", lines_r)

        #lines_y = sum(self.r_and == 0)
        #lines_y = sum(self.pieces_r & FOURS == 0)
        lines_y = self.get_lines_y(self.pieces_r)
        #print("Y Left:", lines_y)


        return lines_r - lines_y


    @lru_cache(maxsize=1024)
    def get_lines_r(self, pieces_y):
        #return sum(self.pieces_y & self.FOURS_y == 0)
        return sum(self.pieces_y & FOURS == 0)

    @lru_cache(maxsize=1024)
    def get_lines_y(self, pieces_r):
        #return sum(self.pieces_r & self.FOURS_r == 0)
        return sum(self.pieces_r & FOURS == 0)



