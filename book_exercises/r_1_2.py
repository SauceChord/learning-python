# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return k & 1 == 0

def print_is_even(k):
    print ("is_even (k={}) == {}".format(k, is_even(k)))

# test some cases
print_is_even(-2)
print_is_even(-1)
print_is_even(0)
print_is_even(1)
print_is_even(2)
print_is_even(3)
