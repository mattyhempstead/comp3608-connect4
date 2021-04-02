import sys, time
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
move = minimax.move(board, player, depth)
#print(move)
print(move[0])

#print("Nodes checked", minimax.nodes_checked)
print(minimax.nodes_checked)

#print(f"Time: {1000*(time.time() - start_time):.8f}ms")



