#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Homework # 2 : Functions
'''
#Details:
#Let's return to the music example from assignment one. Pick 3 of the attributes you listed. For our example we're going to say "Genre", "Artist" and "Year". 
#Create a new Python file and create 3 functions with the same name as those attributes. 
#So in this example we'd have one function named "genre" another named "artist" and another called "year".
#When someone calls any of those functions, that function should return the corresponding value for that attribute. 
#For example, if we call the "Artist" function our function would return "Dave Brubeck". Yours should return whatever values make sense for your music choice.
#One of the data types we haven't covered yet is called "booleans". When a variable is set to True or False, that's a boolean. 
#See if you can figure out how to use booleans, and add an extra function that returns a boolean value instead of a String or Number. 



def Genre():
    genrefnc="Folk Pop"
    return genrefnc

def Artist():
    artistfnc="Ed Sheeran"
    return artistfnc

def Year():
    yearfnc=2017
    return yearfnc

print(Genre())
print(Artist())
print(Year())

#Booleans
def boolean():
    result=Year()==2017
    return result

print(boolean())


# In[ ]:




