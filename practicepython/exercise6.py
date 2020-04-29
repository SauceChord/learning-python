# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

text = input("Provide a string: ")
reverse = text[::-1]

if text == reverse:
    print ("that was a palindrome")
else:
    print ("that wasn't a palindrome")