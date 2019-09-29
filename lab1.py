import numpy as np
V = [[0 ,0 ,0 ,0 ,0],
[1,  0,  1,  0,  1],
[0,  1,  0,  1,  0],
[1,  1,  1,  1,  1]]
print(V)
V1 = []
for i in range(1,5):
    for j in range(i+1,5):
        print("(",i , "," , j ,")")
