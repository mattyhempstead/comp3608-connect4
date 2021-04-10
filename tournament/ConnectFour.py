import sys, time, math

from boards.Board import Board
from boards.BoardBitwise import BoardBitwise
from boards.BoardBitwiseLines import BoardBitwiseLines

from bots.Minimax import Minimax
from bots.MinimaxHorizon import MinimaxHorizon

start_time = time.time()

state = sys.argv[1]
#print(state)

player = 1 if sys.argv[2] == "red" else -1
#print(player)

ab = sys.argv[3] == "A"
#print(ab)

depth = int(sys.argv[4])
#print(depth)


#board = Board(state)
#board = BoardBitwise(state)
board = BoardBitwiseLines(state)
print(board)
#print(board.grid)


#minimax = Minimax()
minimax = MinimaxHorizon()

print(type(board), type(minimax))


#move = minimax.move(board, player, depth, -math.inf, math.inf)

if player == 1:
    move = minimax.move_max(board, depth, -math.inf, math.inf)
else:
    move = minimax.move_min(board, depth, -math.inf, math.inf)

print(move)

print("Nodes checked", minimax.nodes_checked)
print("Nodes eval", minimax.nodes_eval)

print(f"Time: {1000*(time.time() - start_time):.8f}ms")


#print(board.get_lines_r.cache_info())
#print(board.get_lines_y.cache_info())
print(board.get_r_win.cache_info())
print(board.get_y_win.cache_info())





