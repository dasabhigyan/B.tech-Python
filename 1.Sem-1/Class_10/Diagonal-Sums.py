n = int(input())
matrix = []
i = 0 
while i < n:                 
    l = list(map(int, input().split()))
    matrix.append(l)
    i += 1


j = 0 
dia_sum = 0
while j < n:
    dia_sum += matrix[i][i]
    j += 1 
print(dia_sum)