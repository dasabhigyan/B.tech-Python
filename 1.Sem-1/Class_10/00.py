# l = []
# n = int(input())
# i = 0
# while i<n:
#     x = int(input())
#     l,append(x)
#     i += 1



# l = [[1, 2, 3], [0, 8], [7, 6, 5, 4]]
# sum = 0
# i = 0 
# while i < len(l):
#     j = 0
#     while j < len(l[i]):
#         sum += l[i][j]
#         j += 1
#     i += 1
# print(f"The total sum is {sum}.")



l = [[1, 2, 3], [0, 8], [7, 6, 5, 4]]
sum = 0
i = 0 
while i < len(l):
    j = 0
    while j < len(l[i]):
        sum += l[i][j]
        j += 1
    i += 1
    print(f"The total sum is {sum}.")
