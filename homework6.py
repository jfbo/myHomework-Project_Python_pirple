#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 6 : Advance Loops
'''
#Create a function that takes in two parameters: rows, and columns, both of which are integers. 
#The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified. 
#After drawing the board, your function should return True.
#Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. 
#If someone passes a value greater than either maximum, your function should return False.



#x-row(height)
#y-column(width)

def board(x,y):
    
    #maximum width and height that my terminal and screen can fit
    #width=120,height=24
    if x <= 24 and y <= 120:
    
        #for odd number inputs
        if x % 2 != 0 and y % 2 != 0:
            for row in range(x):
                if row % 2 == 0:
                    for column in range(1, y + 1):
                        if column % 2 == 1:
                            if column != y:
                                print(" ", end = "")
                            else:
                                print(" ")
                        else:
                            print("|", end = "")
                else:
                    print("-" * y)

        #for even number inputs
        elif x % 2 == 0 and y % 2 == 0:
            for row in range(x):
                if row % 2 == 0:
                    for column in range(1, y):
                        if column % 2 == 1:
                            if column != y - 1:
                                print(" ", end = "")
                            else:
                                print(" ")
                        else:
                            print("|", end = "")
                else:
                    print("-" * y)

        else:
            print('Input values should either be both even or odd numbers.')
            return False
    
    #maximum width and height that my terminal and screen can fit
    #width=120,height=24
    else:
        print('Limit Exceeded. Input a lower value')
        return False
    
    return True


# Rows - x | Columns - y
# function | board(x,y)
result = board(24,120)
print(result)

