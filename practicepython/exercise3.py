# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print (i)

# Extra 1
# Instead of printing the elements one by one, make a new list that has all the 
# elements less than 5 from this list in it and print out this new list.

b = [i for i in a if i < 5]
print (b)

# Extra 2
# Write this in one line of Python.

print ([i for i in a if i < 5])

# Extra 3
# Ask the user for a number and return a list that contains only elements from 
# the original list a that are smaller than that number given by the user.

number = int(input("Provide a number: "))
print ([i for i in a if i < number])
