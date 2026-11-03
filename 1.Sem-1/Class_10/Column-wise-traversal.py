num_rows = int(input())
num_column = int(input())
matrix = []
i = 0
while i < num_rows:                 
    l = list(map(int, input().split()))
    matrix.append(l)
    i += 1

col = 0
while col < num_column:
    row = 0 
    sum = 0 
    while row <num_rows:
        sum += matrix[row][col]
        row += 1 
    print(sum)
    col += 1