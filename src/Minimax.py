import math 

class Minimax:
    """
        Take an eval function param.
        How to handle time?
        Either use set depth or 

        Do I always use AB pruning?
        I guess so...


    """
    def __init__(self):
        pass

        self.nodes_checked = 0    


    def move(self, board, turn, depth):
        #print("Move", turn, depth)

        self.nodes_checked += 1


        if depth == 0:
            return board.eval()
        
        
        best_move = None
        best_score = -math.inf
        for c in range(7):
            r = board.column_count[c]
            if r < 6:
                # Can expand this branch
                # Move in column c
                board.place(turn, r, c)
                #print(board)

                score = self.move(board, turn*-1, depth-1) * turn

                # Undo move in column c
                board.remove(r, c)



                if score > best_score:
                    best_move = c
                    best_score = score

        #print("Best move", best_move, best_score)
        return best_score








