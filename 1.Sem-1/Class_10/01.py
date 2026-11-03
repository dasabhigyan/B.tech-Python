# how to take m x n matrix as an input 
m = int(input())
n = int(input())
matrix = []
i = 0
while i < m:
    tmp = []
    j = 0
    while j < n:
        x = int(input())
        tmp.append(x)
        j += 1
    matrix.append(tmp)
    i += 1

i = 0
while i < m:
    j = 0
    while j < n:
        print(m[i][j], end =" ")
        j += 1
    print()
    i += 1
    