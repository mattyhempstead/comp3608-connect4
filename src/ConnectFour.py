import sys
from Board import Board
from Minimax import Minimax

state = sys.argv[1]
print(state)

player = 1 if sys.argv[2] == "red" else -1
print(player)

ab = sys.argv[3] == "A"
print(ab)

depth = int(sys.argv[4])
print(depth)


board = Board(state)
print(board)
print(board.grid)


minimax = Minimax()
move = minimax.move(board, player, depth)
print(move)

