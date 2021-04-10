import math, time

class MinimaxSkips:
    """
        Take an eval function param.
        How to handle time?
        Either use set depth or 

        Do I always use AB pruning?
        I guess so...


    """
    def __init__(self):
        self.max_time = None

        self.nodes_checked = 0


    def move_max(self, board, depth, alpha, beta):
        if time.time() > self.max_time:
            return

        self.nodes_checked += 1

        if depth == 0 or board.move_count == 42 or board.has_winner():
            return (-1, board.eval())

        v = -math.inf
        a = None

        for c in [3,2,4,1,5,0,6]:
            r = board.column_count[c]
            if r == 6: continue
            
            board.place(1, r, c)
            move = self.move_min(board, depth-1, alpha, beta)
            if move == None:
                return
            board.remove(r, c)

            score = move[1]
            if score > v:
                v = score
                a = c

            if v >= beta:
                return (c, v)
            alpha = max(alpha, v)
      


        # Try skip
        board.move_count += 1
        move = self.move_min(board, depth-1, alpha, beta)
        if move == None:
            return
        board.move_count -= 1
        score = move[1]
        if score > v:
            v = score
            a = 8
        if v >= beta:
            return (8, v)
        alpha = max(alpha, v)


        return (a,v)


    def move_min(self, board, depth, alpha, beta):
        if time.time() > self.max_time:
            return

        self.nodes_checked += 1

        if depth == 0 or board.move_count == 42 or board.has_winner():
            return (-1, board.eval())

        v = math.inf
        a = None

        for c in [3,2,4,1,5,0,6]:
            r = board.column_count[c]
            if r == 6: continue

            board.place(-1, r, c)
            move = self.move_max(board, depth-1, alpha, beta)
            if move == None:
                return
            board.remove(r, c)

            score = move[1]
            if score < v:
                v = score
                a = c

            if v <= alpha:
                return (c, v)
            beta = min(beta, v)
       

        # Try skip
        board.move_count += 1
        move = self.move_max(board, depth-1, alpha, beta)
        if move == None:
            return
        board.move_count -= 1
        score = move[1]
        if score < v:
            v = score
            a = 8
        if v <= alpha:
            return (8, v)
        beta = max(beta, v)


        return (a,v)







