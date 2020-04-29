# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import date

def age100(current_age):
    return date.today().year + 100 - current_age

user_name = input("Your name: ")
user_age = int(input("Your age: "))

print ("Hi {0}, you will turn 100 year {1}".format(user_name, age100(user_age)))