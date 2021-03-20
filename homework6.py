#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 6 : Advance Loops
'''

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

