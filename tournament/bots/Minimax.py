import math, time

class Minimax:
    """
        Take an eval function param.
        How to handle time?
        Either use set depth or 

        Do I always use AB pruning?
        I guess so...


    """
    def __init__(self):
        self.max_time = math.inf

        self.nodes_checked = 0
        self.nodes_eval = 0


    def move_max(self, board, depth, alpha, beta):
        if time.time() > self.max_time:
            return

        self.nodes_checked += 1

        if depth == 0 or board.move_count == 42 or board.is_y_win():
            self.nodes_eval += 1
            return (-1, board.eval())

        v = -math.inf
        a = None

        for c in [3,2,4,1,5,0,6]:
            r = board.column_count[c]
            if r == 6: continue
            
            board.place(1, r, c)
            #print(board)
            move = self.move_min(board, depth-1, alpha, beta)
            if move == None:
                return
            board.remove(1, r, c)

            score = move[1]
            if score > v:
                v = score
                a = c

            if v >= beta:
                return (c, v)
            alpha = max(alpha, v)
       
        return (a,v)


    def move_min(self, board, depth, alpha, beta):
        if time.time() > self.max_time:
            return

        self.nodes_checked += 1

        if depth == 0 or board.move_count == 42 or board.is_r_win():
            self.nodes_eval += 1
            return (-1, board.eval())

        v = math.inf
        a = None

        for c in [3,2,4,1,5,0,6]:
            r = board.column_count[c]
            if r == 6: continue

            board.place(-1, r, c)
            #print(board)
            move = self.move_max(board, depth-1, alpha, beta)
            if move == None:
                return
            board.remove(-1, r, c)

            score = move[1]
            if score < v:
                v = score
                a = c

            if v <= alpha:
                return (c, v)
            beta = min(beta, v)
       

        return (a,v)







