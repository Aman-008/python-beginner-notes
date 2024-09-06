# # Update the '_' to solve the problem

# n = int(input())
# a = 0
# b = 1

# print(a, b, end=" ")

# count = 1

# for i in range(n-2):
#     c = a+b # set currrent number as sum of previous two numbers
#     print(c, end=" ")
#     # Update a and b as next two numbers
#     a = b 
#     b = c




n = int(input())
# Solution as follows
first, second = 0, 1
for i in range(n):
    print(first, end=" ")
    next = first + second
    first = second
    second = next