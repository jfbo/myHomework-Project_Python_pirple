#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 5 : Basic Loops
"Fizz Buzz"
'''

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

