num_rows = int(input())
num_column = int(input())
matrix = []
i = 0
while i < num_rows:                 
    l = list(map(int, input().split()))
    matrix.append(l)
    i += 1


row = 0 
while row <num_rows:
    col = 0 
    sum = 0 
    while col < num_column:
        sum += matrix[row][col]
        col += 1
    print(sum)
    row += 1
