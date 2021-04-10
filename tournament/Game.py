import math, time, random
from Board import Board

class Game:
    """
        Competes two bots against one another
    """

    def __init__(self):
        pass


    def compete(self, player1, player2):
        board = Board(",".join(["."*7]*7))
        #board = Board(".ryyrry,.rryry.,..y.r..,..y....,.......,.......")

        bot1, board1 = player1
        bot2, board2 = player2

        turn = 1

        while True:
            start_time = time.time()

            move_time = 0.5 + random.random()*1.0
            #move_time = 1

            if turn == 1:
                print("Player 1 move")
                bot1.max_time = start_time + move_time
                board_bot = board1(board.get_state_str())
            else:
                print("Player 2 move")
                bot2.max_time = start_time + move_time
                board_bot = board2(board.get_state_str())


            # IDS to get move
            i = 1
            best_move = None
            while True:
                if turn == 1:
                    move = bot1.move_max(board_bot, i, -math.inf, math.inf)
                else:
                    move = bot2.move_min(board_bot, i, -math.inf, math.inf)

                # Keep going deeper until we run out of time
                if move == None:
                    break
                else:
                    print(i, move, f"{1000*(time.time() - start_time):.8f}ms")
                    best_move = move
                    i += 1
                    
                    if abs(best_move[1]) >= 10000 or i+board.move_count>42:
                        break

            print(f"Move time: {1000*(time.time() - start_time):.8f}ms")
           
            # Make move on game board
            if best_move[0] == 8:
                board.skip()
            else:
                board.place(
                    turn, 
                    board.column_count[best_move[0]],
                    best_move[0]
                )
            print(board)

            # Check if game board has winner or is finished
            if board.has_winner():
                return turn
            elif board.move_count == 42:
                return 0

            turn *= -1



