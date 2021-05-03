#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 5 : Basic Loops
"Fizz Buzz"
'''
#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".
#Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime". 
#You should print this whenever you encounter a number that is prime (divisible only by itself and one).



# code showing numbers involved with "fizz", "buzz", "fizzbuzz", and "prime"
for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print(numbers, "FizzBuzz")
    elif numbers % 3 == 0:
        print(numbers, "Fizz")
    elif numbers % 5 == 0:
        print(numbers, "Buzz")
    #looking for prime numbers
    elif numbers % 2 != 0 and numbers % 3 != 0:
        print(numbers, "prime")

print()        
        
# code showing all numbers from 1 - 100
for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print(numbers, "FizzBuzz")
    elif numbers % 3 == 0:
        print(numbers, "Fizz")
    elif numbers % 5 == 0:
        print(numbers, "Buzz")
    #looking for prime numbers
    elif numbers % 2 != 0 and numbers % 3 != 0:
        print(numbers, "prime")
    else:
        print(numbers)

