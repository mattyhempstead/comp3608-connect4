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

        if depth == 0:
            return (-1, board.eval())

        v = -math.inf
        a = None

        for c in range(7):
        #for c in range(7:
            r = board.column_count[c]
            if r == 6: continue
            
            board.place(1, r, c)
            score = self.move_min(board, depth-1, alpha, beta)[1]
            #winner = board.is_winner()
            #if winner:
            #    score = turn * 10000
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

        if depth == 0:
            return (-1, board.eval())

        v = math.inf
        
        for c in range(7):
            r = board.column_count[c]
            if r == 6: continue
            
            board.place(-1, r, c)
            score = self.move_max(board, depth-1, alpha, beta)[1]
            #winner = board.is_winner()
            #if winner:
            #    score = turn * 10000
            board.remove(r, c)

            if score < v:
                v = score
                a = c

            if self.ab and v <= alpha:
                return (c, v)
            beta = min(beta, v)
        
        return (a,v)



    def move(self, board, turn, depth, alpha, beta):
        #print("Move", turn, depth)

        self.nodes_checked += 1


        if depth == 0:
            return (-1, board.eval())
        
        
        best_move = None
        best_score = -math.inf * turn
        for c in range(7):
            r = board.column_count[c]
            if r < 6:
                # Can expand this branch
                # Move in column c
                board.place(turn, r, c)
                #print(board)

                #print("Place", turn, depth, c)
                score = self.move(board, turn*-1, depth-1, alpha, beta)[1]
                #print(c, score)

                #winner = board.is_winner()
                #if winner:
                #    score = turn * 10000

                # Undo move in column c
                board.remove(r, c)

                # maximise
                if turn == 1:
                    if score > best_score:
                        best_move = c
                        best_score = score
                        
                        if self.ab:
                            alpha = score
                            if score >= beta:
                                #print("Beta cutoff")
                                break

                else:
                    if score < best_score:
                        best_move = c
                        best_score = score

                        if self.ab:
                            beta = score
                            if score <= alpha:
                                #print("Alpha cutoff")
                                break

                #if winner: break

                #if turn*score > turn*best_score:
                #    best_move = c
                #    best_score = score
        
        #print("Best move", best_move, best_score)
        return (best_move, best_score)








