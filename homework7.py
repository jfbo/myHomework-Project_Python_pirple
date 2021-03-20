#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 7 : Dictionaries and Sets
'''

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

