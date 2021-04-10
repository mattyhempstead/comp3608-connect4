import time
from Game import Game
from bots.Minimax import Minimax
from bots.MinimaxSkips import MinimaxSkips

from Board import Board
from BoardBitwise import BoardBitwise

start_time = time.time()

game = Game()


player1 = (Minimax(), Board)
player2 = (Minimax(), BoardBitwise)


f = open("results.csv", "w")
f.write("a,b\n")
f.close()

while True:
    result = game.compete(player1, player2)
    print("First winner:", result)
    with open("results.csv", "a") as f:
        f.write("f," + str(result) + "\n")

    result = game.compete(player2, player1) * -1
    print("Second winner:", result)
    with open("results.csv", "a") as f:
        f.write("s," + str(result) + "\n")



print(f"Time: {1000*(time.time() - start_time):.8f}ms")

