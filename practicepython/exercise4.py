# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input ("Find divisors for number: "))
divisors = [i for i in range (1, number + 1) if number % i == 0]
print (divisors)