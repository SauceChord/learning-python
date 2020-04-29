# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print (list(set(a) & set(b)))

# Extra 1:
# Randomly generate two lists to test this

c = [random.randrange(20) for i in range(15)]
d = [random.randrange(20) for i in range(15)]

print ("list c {}".format(c))
print ("list d {}".format(d))
print ("common between c and d {}".format(list(set(c) & set(d))))

# Extra 2:
# Write this in one line of Python (don’t worry if you can’t figure this 
# out at this point - we’ll get to it soon)

print(list(set([random.randrange(20) for i in range(15)]) & set([random.randrange(20) for i in range(15)])))