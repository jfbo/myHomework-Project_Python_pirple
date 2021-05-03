"""
Homework # 10 : Importing
"""
#Pick any library that come with Python (https://docs.python.org/3/library/) that we haven't covered in the course already.
#Learn how to use the library extensively, then prepare a code sample that showcases what you've learned. This can take any form you wish. 
#You could create an application with the library, or just show examples of how to use its methods.



# https://docs.python.org/3/library/
# https://docs.python.org/3/library/turtle.html
import turtle

Window_ = turtle.Screen()
Window_.bgcolor("light blue")
Window_.title("Let's Draw a Polygon")

polygon_ = turtle.Turtle()

"""
Using the library 'turtle'
The function will draw the desired polygon based on the number of sides entered.
Reference about drawing shapes: https://www.educba.com/python-turtle/
"""
def TurtlePolygon():
    polygons = {}
    #polygons = {sides : [interior angle, polygon term, pixel length]}
    polygons[3] = [240, 'Triangle', 150]
    polygons[4] = [270, 'Quadrilateral', 125]
    polygons[5] = [288, 'Pentagon', 100]
    polygons[6] = [300, 'Hexagon', 100]
    polygons[7] = [308.5, 'Heptagon', 75]
    polygons[8] = [315, 'Octagon', 50]
    polygons[9] = [320, 'Nonagon', 50]
    polygons[10] = [324, 'Decagon', 50]

    sides = int(input("Enter number of sides of polygon (3 - 10): "))
    for key in polygons:
        if key == sides:
            print("A", polygons[key][1], "has", key, "sides.")
            angles = polygons[key][0]
            size = polygons[key][2]
            for i in range(sides):
                polygon_.forward(size)
                polygon_.right(angles)

TurtlePolygon()

decision = True
while (decision == True):
    choice = str(input('Clear drawing? ["yes"/"no"]:  '))
    if choice == "yes":
        turtle.resetscreen()
        TurtlePolygon()
    else:
        turtle.bye()
        decision = False
