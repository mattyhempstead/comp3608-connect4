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



Tournament version should really only care about open n-in-a-rows (unless its a
4-in-a-row, which gets max weight). Any 2 or 3 lines that are fully blocked up
should not be worth anything.
Could maybe weight the columns or direction of line differently.




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


Need a fast bitwise_and



## Alpha Beta
I think we always want to first scan the nodes that are best for the current player.
Probably start from the middle then.



## Bugs
If board is almost full bot will error



 . . . x . . .
 . . o o o . .
 . . x o o o .
 . . x o x x .
 . x x x o o .
 . x o x x o .

On this position bot chooses to play 0 rather than 5 at depth 3.
1 (1, 101) 0.47373772ms
2 (5, -200) 1.15132332ms
3 (0, 201) 3.64995003ms
4 (5, -100) 11.60883904ms
5 (1, 291) 31.35657310ms
6 (5, 0) 88.59562874ms
7 (1, 291) 211.83156967ms
8 (0, 100) 542.55199432ms







## Simulator
Need to make it non-determinsitic to get indiction of win rate.

Can try randomly swapping between looping on [3,2,4,1,5,0,6] and [3,4,2,5,1,6,0]
as this should slightly change rate of search.

Prob not.

Instead limit time randomly between 0.8 and 1.2 seconds?



## Optimal Moves
Get a big move bank of optimal moves.

Without skips, I could easily get the first 6 or so moves.

With skips however, the optimal move is much less obvious and might require some
large searches?



## Bitwise

Store game state as two 42 bit strings.
Represent opponent and my moves.

Get a list of all possible 4-in-a-rows as bit strings.
I count 69.

Can check easily with bit-wise operations if board has a given winning state.
Invert winning state. OR with player board. Check for all ones.

Using opponents bits, I can count how many possible 4-in-a-rows still exist.
Can find how many still exist for opponent too.


Maybe also different 4-in-a-row combinations are worth more than others.
Can weight them differently in the score.
This gives the GA something to train for.



Could also look for other features (e.g. L's).
Pretty time consuming but possible.

Having two winning placements above eachother is a certain win feature.
Also a placement which opens up two winning placements is a certain win.



 . . . x . . .
 . . o o o . .
 . . x o o o .
 . . x o x x .
 . x x x o o .
 . x o x x o .

 3*7 + 4*6 + 3*4 + 3*4 = 69

For opponent and me, this gives 138 checks (weights).



## Features

Could create features which represent combinations of 4-in-a-rows.
 . . . . . . .
 . . x x x x .
 . . . . . x .
 . . . . x . .
 . . . x . . .
 . . x . . . .

e.g. This one represents a winning situation against a skip bot.



## Search Order

Currently searching from middle out.
Could pick sort order based on how many 4-in-a-rows pass through that column?
This would only be a single scan at the init of the bot.



## Control Strategy
Try the quickest possible strategy 4-in-a-rows.
This involves just placing pieces in order and searching for a 4-in-a-row.
Checking is pretty slow. Could maybe try the check method that looks at
surrounding pieces only when a piece is placed.



At the start filter out the 4-in-a-rows that are impossible for each player?
All future checks will be shorter.

Maybe the higher depths can move 4-in-a-rows out of the array?

Checking for winner can be simplified.
I only need to check for those 4-in-a-rows passing through the recently placed
piece.
Can do this when I placed the piece itself.


## Speed 2

Hard code the final depth check.
This prevents another function call and might be a bit quicker?



If we reach a winning node for current player, return instantly and stop
searching? I think ab isn't fully efficient here.



## lru_cache
Wow so good.
The IDS will now be so much faster since its all the same program?
Make sure its the same board!

The same function across different instances might break?




## Evaluation Function
Gotta be quick and good.

Try giving each position on the board a worth.
Pieces closer to the centre are generally worth more (can be learned).
To evaluate the pieces we sum up our own and subtract the opponents.
Maybe start by having the value be the total numebr of lines a piece provides?



## Simulation
Plot winning % vs search time (with error)?


## Search Order



