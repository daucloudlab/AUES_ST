# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
print("Salem!")

# %% [markdown]
# print(value1, value2, value3)

# %%
print("Hello", "Salem", 12, 6+5, 5.6)

# %% [markdown]
# print(value1, end='\n')

# %%
print("Salem")
print("Hello")
print("Welcome")


# %%
print("Salem", "Hello", "Welcome", end = " ")


# %%
print("Salem", end = " ")
print("Hello", end = "--")
print("Welcome", end= "!")

# %% [markdown]
# print(value1, value2, value3, sep=" ")

# %%
print("Salem", "Hello", "Welcome", sep = "---")

# %% [markdown]
# strobject.format(value1, value2)

# %%
print("{0:.3f}".format( 3.1415926))


# %%
print(f'{0}', 3.1415)


# %%
import math

# %% [markdown]
# math.pow(2,3)
# math.sqrt(2)
# math.fabs(12)
# math.sin(0.12)
# %% [markdown]
# /
# //
# %

# %%
7/5


# %%
7 // 5


# %%
7 % 5


# %%
import math
math.ceil(2.3)


# %%
math.ceil(2.8)


# %%
math.floor(2.3)


# %%
math.floor(2.8)


# %%
a = input("Енгізіңіз ")


# %%
a


# %%
type(a)


# %%
a = int(a)


# %%
a


# %%
type(a)


# %%
a = int(input())
b = float(input())


# %%
a


# %%
b


# %%
type(a)


# %%
type(b)

# %% [markdown]
# 
#    if condition:
#        operators
#    elif condition:
#        operators
#    elif:
#         operators
#    else:
#         operators
# 

# %%
for i in range(11):
    print(i, end = ' ')


# %%
i = 0
while i < 10:
    if i == 5:
        print("Операторлар")
    i += 1


# %%
for i in range(1, 11):
    if i == 5:
        print("Операторлар")


# %%
i = 1
sum = 0
while i <= 3:
    a = int(input("Бүтін санды енгіз: "))
    sum += a
    i += 1
print("sum = ", sum)


# %%
for i in range(4):
    for j in range(3):
        print(8, end = " ")
    print()


# %%
for i in range(1,8):
    for j in range(5):
        print(i, end = " ")
    print()


# %%
import random


# %%
random.random()


# %%
random.randint(2, 5)


# %%
random.randrange(2, 5)


# %%
random.choice([2,4,5,10])


# %%
for i in range(8):
    print(random.random())


# %%
int(random.random()*10)+1


# %%
int(random.random()*10)+1


# %%



