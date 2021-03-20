#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 4 : Lists
'''

#Global Variable
myUniqueList = []
myLeftovers = []

def addthings(things):
    if things not in myUniqueList:
        myUniqueList.append(things)
        return True
    else:
        #to be added instead to 'myLeftovers' variable
        myLeftovers.append(things)
        return False

#some values are printed to double check duplicates    
addthings(1)
print(addthings(2))
addthings(3.14)
print(addthings(2))
print(addthings('hello'))
addthings('world')
addthings('python')
print(addthings('hello'))

#Final Lists generated
print('myUniqueList: ', myUniqueList)
print('myLeftovers: ', myLeftovers)

