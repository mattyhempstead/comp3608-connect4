import math, time

class MinimaxHorizon:
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


        if depth > 1:
            # Play on instant wins (with higher priority)
            for c in [3,2,4,1,5,0,6]:
                r = board.column_count[c]
                if r == 6: continue

                board.place(1, r, c)
                if board.is_r_win():
                    ret = (c, board.eval())
                    board.remove(1, r, c)
                    return ret
                board.remove(1, r, c)


            # Play to block instant losses
            for c in [3,2,4,1,5,0,6]:
                r = board.column_count[c]
                if r == 6: continue
           
                board.place(-1, r, c)
                if board.is_y_win():
                    board.remove(-1, r, c)

                    # Assume all other moves result in loss
                    board.place(1, r, c)
                    move = self.move_min(board, depth-1, alpha, beta)
                    if move == None:
                        return
                    ret = (c, move[1])
                    board.remove(1, r, c)
                    return ret
                board.remove(-1, r, c)



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
            #print("Score", move)
            if score > v:
                #print("Greater than", v)
                v = score
                a = c

            if v >= beta:
                #print("Beta skip", v, beta)
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


        if depth > 1:
            # Play on instant wins (with higher priority)
            for c in [3,2,4,1,5,0,6]:
                r = board.column_count[c]
                if r == 6: continue

                board.place(-1, r, c)
                if board.is_y_win():
                    ret = (c, board.eval())
                    board.remove(-1, r, c)
                    return ret
                board.remove(-1, r, c)


            # Play to block instant losses
            for c in [3,2,4,1,5,0,6]:
                r = board.column_count[c]
                if r == 6: continue
           
                board.place(1, r, c)
                if board.is_r_win():
                    board.remove(1, r, c)

                    # Assume all other moves result in loss
                    board.place(-1, r, c)
                    move = self.move_max(board, depth-1, alpha, beta)
                    if move == None:
                        return
                    ret = (c, move[1])
                    board.remove(-1, r, c)
                    return ret
                board.remove(1, r, c)



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
            #print("Score", move)
            if score < v:
                #print("Less than", v)
                v = score
                a = c

            if v <= alpha:
                #print("Alpha skip", v, alpha)
                return (c, v)
            beta = min(beta, v)
       

        return (a,v)







