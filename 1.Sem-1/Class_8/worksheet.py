# i = 1
# while i!=6:
#     print(i)
#     i = i +2
# print("Mid-sem is coming........")

# n = int(input())
# i = 1

# while i <=n:
#     print(i)
#     i = i+2
# print(i)

# while True:
#     cmd = input("cmd> ")
#     if cmd == "quit":
#             print("bye")
#             break
#     print("you said:", cmd)


# i = 0 
# while True:
#     print(i)
#     i =i+1
#     if i == 5:
#         break
#     print(i)
# print(i)


# #Question 
# while True:
#     password = input("")
#     if password == "open sesame":
#         print("Unlocked")
#         break
#     else:
#         print("Wrong Password, Try again")



# #Question: Password with 5 attempts.
# i = 5
# while i>=0:
#     password = input()
#     if password != "1332":
#         i = i-1
#         print("Wrong password attempts remainig", i)
#         if i==0:
#             break
#     else:
#         print("Unlocked")
#         break




# #Question(puzzle): Number Of Open Doors after n Toggles
# import math
# n = int(input())
# print(int(math.sqrt(n)))


# #Question: Given an integer n (with n >= 0 ), print n! — that is 1 x 2 x 3 x ... x n . By definition 0! = 1 .
# n = int(input())
# i = 1
# ans = 1
# while i<=n:
#     ans = ans*i
#     i+=1
# print(ans)

# n = int(input())
# i = 1
# c = 0
# while i<=n:
#     if n%i ==0:
#         c +=1
#     i +=1

# if c == 2:
#     print("Prime number")
# else:
#     print("Not a Prime number")



# #Question: expansion of e power x series:
x = float(input("Enter x: "))
n = int(input("Enter number of steps: "))

total = 0
term = 1
i = 1

while i <= n:
    total += term
    term = term * x / i
    i += 1
print(total)


#Question: Sine Value Expantion:
