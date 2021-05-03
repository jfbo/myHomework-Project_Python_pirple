'''
Homework # 3 : "If" Statements
'''
#Details:
#Create a function that accepts 3 parameters and checks for equality between any two of them.
#Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
#Modify your function so that strings can be compared to integers if they are equivalent. 
#For example, if the following values are passed to your function: 6,5,"5"
#You should modify it so that it returns true instead of false.



def function(a,b,c):
    
    #"int" to convert strings to integers
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a==b or b==c or a==c:
        equality = True
    else:
        equality = False
    
    return equality

#Parameters : 6 , 5 , "5"
result = function(6,5,"5")

print(result)