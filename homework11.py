'''
Homework # 11 : Error Handling
'''
#For this assignment you can choose any of the homeworks or projects you've done so far. 
#Pick a function that you know is particularly problematic and add try/except/finally cases to it so that it can handle the errors more gracefully.
#Below your function, add 10 - 20 tests that call your function in different ways, and show that it can now handle various different conditions and cases.


'''
Applying "Error Handling" to homework # 3
Code of my previous homework...

Homework # 3 : "If" Statements

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
'''

def function(a, b, c):
    try:
        equality = False
        a = int(a)
        b = int(b)
        c = int(c)
        
        if a==b or b==c or a==c:
            equality = True

    except ValueError:
        print("ValueError: Integers only!")
    except TypeError:
        print("TypeError: Integers only!")
    except Exception:
        print("Exception: Integers only!")
    finally:
        return equality

#Testing different parameters
print(function(0, 1, 2), "\n")
print(function(0.0, 1.1, 2.2), "\n")
print(function(1, 1, 1), "\n")
print(function('1', '1', '1'), "\n")
print(function('0', '1', '2'), "\n")
print(function('a', 'b', 'c'), "\n")
print(function(' ', ' ', ' '), "\n")
print(function(0, 1, True), "\n")
print(function(0.1, ' ', 'True'), "\n")
print(function(0, '1', [True]), "\n")

