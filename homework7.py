#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 7 : Dictionaries and Sets
'''
#Return to your first homework assignments, when you described your favorite song. Refactor that code so all the variables are held as dictionary keys and value. 
#Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.
#Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. Parameters: Key and Value
#If the key exists in the dictionary and that value is the correct value, then the function should return true. In all other cases, it should return false.



song = {
    "artist": "Ed Sheeran", 
    "genre": "Folk Pop", 
    "album": "Divide", 
    "month released": 
    "September", 
    "duration in seconds": "263", 
    "year released": "2017", 
    "duration in minutes": "4.28"
}

print(song, "\n")

for key in song:
    print(key, ":", song[key],)

print()    

def function(key,value):
    if key in song and song[key] == value:
        print("You are correct!")
    else:
        print("Wrong guess.")
        return False
    return True

function(input("Enter Key: "),input("Enter Value: "))

