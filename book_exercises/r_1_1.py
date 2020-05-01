# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n, m):
    return n % m == 0

def print_is_multiple(n, m):
    print("is_multiple (n={}, m={}) == {}".format(n, m, is_multiple(n, m)))

print_is_multiple(4, 1)
print_is_multiple(4, 2)
print_is_multiple(4, 3)
print_is_multiple(4, 4)
print_is_multiple(4, 8)