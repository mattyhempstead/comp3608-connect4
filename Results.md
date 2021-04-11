# Results


IDS Minimax vs IDS Minimax.
990ms to decide.
50 games, 2nd player wins every time.

800-1200ms to decide.
22 games, 2nd player wins every time.

500-1500ms to decide.
82 games, 2:80



500-1500ms to decide.
1: Minimax
-1: Minimax with skips
f  -1    283
    0    462
    1    134
s  -1    543
    0     25
    1    310







500-1500ms to decide

no-cache bitwiselines VS regular
f  -1    17
s  -1     8
    1     9


cache bitwise VS regular
f  -1    14
s  -1    11
    1     2

cache bitwiselines vs regular
f  -1    47
s  -1    33
    0     2
    1    12

cache bitwise vs cache bitwiselines
f  -1     9
    0    10
    1    75
s  -1    38
    0    42
    1    14



cache bitwise horizon vs cache bitwiselines horizonwin
f  -1    16
    0     3
    1    14
s  -1    13
    0    15
    1     4


cache bitwise vs cache bitwiselines horizonwin
f  -1    16
    0     1
    1     6
s  -1     6
    0    14
    1     2


regular VS cache bitwise horizonwin
f  -1    51
s  -1    41
    1    10



regular VS cache bitwise
f  -1    112
s  -1     88
    0      2
    1     21

f  -1    0.502242
s  -1    0.394619
    0    0.008969
    1    0.094170

223


regular VS cache bitwise piece
f  -1    144
s  -1    117
    0      6
    1     20

f  -1    0.501742
s  -1    0.407666
    0    0.020906
    1    0.069686

287


regular VS cache bitwise piece horizon
f  -1    244
s  -1    192
    0     17
    1     34
dtype: int64
a  b 
f  -1    0.501027
s  -1    0.394251
    0    0.034908
    1    0.069815
dtype: float64
487


cache bitwise VS cache bitwisepiece horizon
a  b 
f  -1     91
    0    172
    1     37
s  -1    299
dtype: int64
a  b 
f  -1    0.151920
    0    0.287145
    1    0.061770
s  -1    0.499165
dtype: float64
599


cache bitwise VS cache bitwiselines horizon
a  b 
f  -1    220
    0     14
    1    128
s  -1    142
    0    176
    1     44
dtype: int64
a  b 
f  -1    0.303867
    0    0.019337
    1    0.176796
s  -1    0.196133
    0    0.243094
    1    0.060773
dtype: float64
724


cache bitwise VS cache bitwise horizon
a  b 
f  -1    277
s   1    277
dtype: int64
a  b 
f  -1    0.5
s   1    0.5
dtype: float64
554



cache bitwiselines horizon VS cache bitwisepiece horizon
a  b 
f  -1     681
    0     342
    1      51
s  -1    1003
    0      13
    1      58
dtype: int64
a  b 
f  -1    0.317039
    0    0.159218
    1    0.023743
s  -1    0.466946
    0    0.006052
    1    0.027002
dtype: float64
2148


