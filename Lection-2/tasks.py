# task 5.1
# i = 1
# while i <= 10:
#     print(20, end = ' ')
#     i += 1

# print()
# print('-'*30)

# task 5.2
# a = int(input("Input a number: "))
# for i in range(10):
#     print(a, end = ' ')

# task 5.3
# for i in range(20, 35):
#     print(i)

# task 6.2
# n = int(input("Sandy engiz: "))
# for i in range(1, n+1):
#     if i <= n:
#         print(i, end = " ")
#     else:
#         break

# task 6.3
# for i in range(10, 101):
#     if i % 2 != 0:
#         print(i, end = " ")

# # task 6.20
# n = int(input("Sandy engiz: "))
# sum = 0
# counter = 0
# while n:
#     # 125 % 10 -> 5
#     # 125 // 10 -> 12
    
#     # 12 % 10 -> 2
#     # 12 // 10 -> 1

#     # 1 % 10 -> 1
#     # 1 // 10 -> 0
#     sum = sum + n % 10
#     n = n // 10

#     counter = counter + 1

# print("sum = ", sum)
# print("counter = ", counter)

# task 7.1
# sum = 0
# for i in range(10):
#     n = float(input("Sandy engiz: "))
#     sum = sum + n

# print("sum = ", sum)

# task 7.11
# res = 1
# for i in range(8):
#     n = int(input("Sangy engiz: "))
#     res = res * n
# print("res = ", res)

# task 8.1
# n = int(input("Sandy engiz: "))

# for i in range(1, n):
#     if i**2 <= n:
#         print(i**2)

# task 8.2
# n = int(input("Sandy engiz: "))
# i = 1
# while i ** 2 <= n:
#     # print(i**2, end = ' ')
#     i += 1

# print(i)

# # task 9.1a
# for k in range(5):
#     for i in range(3):
#         print(8, end = " ")
#     print()

# task 9.1b
# for i in range(1,8):
#     for k in range(5):
#         print(i, end = " ")
#     print()

# # task 9.1j
# for i in range(5):
#     for k in range(6-i):
#         print(0, end = ' ')
#     print()

# # task 10.1a
# import random
# for i in range(8):
#     print("{0:.2f}".format(random.random()))


# # task 10.1g
# import random
# for i in range(20):
#     print(random.randrange(0, 15), end = " ")
        
# task 10.2a
# import random
# for i in range(10):
#     print(random.randint(0, 10), end = ' ')