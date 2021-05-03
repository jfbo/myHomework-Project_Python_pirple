#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 4 : Lists
'''
#Details:
#Create a global variable called myUniqueList. It should be an empty list to start.
#Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, 
#unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. 
#If the value does exist, it should not be added, and the function should return False;
#Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, 
#and then finally it should print the value of myUniqueList to show that it worked.
#Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. 
#If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.



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

