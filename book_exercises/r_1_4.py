# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_squares (n):
    return sum((i ** 2 for i in range(1, n)))

# 3*3 + 2*2 + 1*1 = 14
print (sum_squares(4))