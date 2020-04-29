# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

text = input("Provide a string: ")
text_len = len(text)
is_palindrome = True

for i in range(0, text_len):
    if (text[i] != text[text_len - i - 1]):
        is_palindrome = False
        break

if is_palindrome:
    print ("that was a palindrome")
else:
    print ("that wasn't a palindrome")