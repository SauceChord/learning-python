# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

parity = ['even', 'odd']
number = int(input("Enter a number: "))

# Extra 1
# If the number is a multiple of 4, print out a different message.

if number % 4 == 0:
    print ("The number is a multiple of 4")
else:
    print ("The number is " + parity[number % 2])

# Extra 2:
# Ask the user for two numbers: one number to check (call it num) and one 
# number to divide by (check). If check divides evenly into num, tell that 
# to the user. If not, print a different appropriate message.

num = int(input("Enter num to check: "))
check = int(input("Enter number to divide by: "))

if num % check == 0:
    print ("num is evenly divisble")
else:
    print ("num is not evenly divisible")