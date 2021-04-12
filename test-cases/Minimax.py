import math 

class Minimax:
    """
        Take an eval function param.
        How to handle time?
        Either use set depth or 

        Do I always use AB pruning?
        I guess so...


    """
    def __init__(self, ab):
        self.ab = ab

        self.nodes_checked = 0


    def move_max(self, board, depth, alpha, beta):
        self.nodes_checked += 1

        if depth == 0 or board.is_terminal():
            return (-1, board.eval())

        v = -math.inf
        a = None

        for c in range(7):
            r = board.column_count[c]
            if r == 6: continue
            
            board.place(1, r, c)
            score = self.move_min(board, depth-1, alpha, beta)[1]
            board.remove(r, c)

            if score > v:
                v = score
                a = c

            if self.ab and v >= beta:
                return (c, v)
            alpha = max(alpha, v)
        
        return (a,v)


    def move_min(self, board, depth, alpha, beta):
        self.nodes_checked += 1

        if depth == 0 or board.is_terminal():
            return (-1, board.eval())

        v = math.inf

        for c in range(7):
            r = board.column_count[c]
            if r == 6: continue
            
            board.place(-1, r, c)
            score = self.move_max(board, depth-1, alpha, beta)[1]
            board.remove(r, c)

            if score < v:
                v = score
                a = c

            if self.ab and v <= alpha:
                return (c, v)
            beta = min(beta, v)
        
        return (a,v)



