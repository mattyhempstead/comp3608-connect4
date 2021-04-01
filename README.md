# Connect4 Bot


Use matrix as board.

When traversing tree.
Place on board.
Only check for impacts that piece could have had.
One option is a bitmask for each piece (probably need a larger board with
blanks surrounding).

Alternatively I manually scan all 4 (8) directions to count length.
Each same coloured node I reach will need to have its direction incremented.
Probably best to not even use a loop. Literally just a bunch of nested if
statements.


When given the board state we do pre-processing to get all the states.
Easy way to do this is to simulate placing all the pieces one at a time?


## A*
With a quick and accurate eval function this could be a much more efficient search.
Especially if I use GA on the eval function.

Basically minimax kinda?



## AB pruning
Can we make this more efficient?




## Evaluation Functions
Use genetic algorithm to find best evaluation functions.
Probably just optimise it against the generic eval function.
Currently eval is just a linear combination of 3-in-a-rows and 2-in-a-rows.
Should take into acccount if they have free edges (how many free edges also matters).

Linear combination could be a matrix multiplication depending on how data is
tracked. Should see how fast that turns out. Probably not tbh.




Could technically do a neural network and then train it to look further ahead?
This would make evaling the leaf nodes quite slow.



## Time Limit
Need to use time wisely.
Maybe use IDS?
After each IDS, check time passed, if more than 0.1s then return current value?
Considering we expect time to multiply by 8x for each extra layer.
Probably plot the times we get and check this is the case.



## Speed
Might be slightly quicker to not have a depth=0 recursive call.
Instead just manually program depth=1 loop 


Technically I don't need to track how many pieces are above.
This is a 12.5% speed up on this section.


Is it actually quicker dynamically tracking relevant board values?
Would it instead be quicker to just calculate them at the leaf nodes?


Read some stuff about putting matrix in cache?
Need to be able to read/write from this SUPER quick.



