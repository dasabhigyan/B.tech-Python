num_rows = int(input())
num_column = int(input())
matrix = []
i = 0
while i < num_rows:                 # in this matrix elements have to separated by spaces 
    l = list(map(int, input().split()))
    matrix.append(l)
    i += 1
print(matrix)
