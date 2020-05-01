# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax (data):
    min = max = data[0]
    for v in data:
        if v < min:
            min = v
        if v > max:
            max = v
    return min, max

sample = [20, 14, 4, 11]

# expect (4, 20)
print (minmax(sample))