import random
from time import time
import numpy as np

A = random.randrange(0,2**42) 
B = random.randrange(0,2**42) 

W = [random.randrange(0,2**42) for i in range(69)]

print(A,B)


W = np.array(W)


t = time()

for i in range(1000000):
    #x = [A&i for i in W]
    #y = [B&i for i in W]

    #x = A & W
    #y = B & W

    x = np.bitwise_or(W,A)
    y = np.bitwise_or(W,A)

print(time() - t)



#print([A&i for i in W])

print(np.bitwise_and(W,A))

