import sys, time, math
from Board import Board
from Minimax import Minimax

start_time = time.time()

state = sys.argv[1]
#print(state)

player = 1 if sys.argv[2] == "red" else -1
#print(player)

ab = sys.argv[3] == "A"
#print(ab)

depth = int(sys.argv[4])
#print(depth)


board = Board(state)
#print(board)
#print(board.grid)


minimax = Minimax(ab)

#move = minimax.move(board, player, depth, -math.inf, math.inf)

if player == 1:
    move = minimax.move_max(board, depth, -math.inf, math.inf)
else:
    move = minimax.move_min(board, depth, -math.inf, math.inf)

#print(move)
print(move[0])

#print("Nodes checked", minimax.nodes_checked)
print(minimax.nodes_checked)

#print(f"Time: {1000*(time.time() - start_time):.8f}ms")



