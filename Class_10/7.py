n = int(input())
i = 1
while i <=n:
    print(" "*(n-i), end="")
    j = 1
    while j <=i:
        print(j, end="")
        j +=1
    j = j-2
    while j> 0:
        print(j, end="")
        j -= 1
    print()
    i +=1