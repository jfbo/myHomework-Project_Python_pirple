"""
Homework # 9 : Classes
"""
#Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
#The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.
#Next an inheritance classes from Vehicle called "Cars".
#The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  
#It should have another method called "Stop" that sets the value of isDriving to false.
#Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. 
#And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.
#Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.
#Create 3 different cars, using your Cars class, and drive them all a different number of times. 
#Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance
#Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), 
#but different in one respect: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected (return false), 
#and an error message should be printed saying that the plane can't fly until it's repaired.



class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintainance = False
        self.TripsSinceMaintainance = 0

    def getMaintainance(self):
        return self.NeedsMaintainance
    def getTripsSinceMaintainance(self):
        return self.TripsSinceMaintainance

    def trip(self):
        if self.TripsSinceMaintainance <= 100:
            self.TripsSinceMaintainance += 1
        else:
            self.NeedsMaintainance = True
    
    def repair(self):
        if self.NeedsMaintainance:
            self.TripsSinceMaintainance = 0
            self.NeedsMaintainance = False
            return True
        else:
            return False


class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False
    
    def Drive(self):
        if not self.isDriving:
            self.isDriving = True
            return True
        else:
            return False

    def Stop(self): 
        if self.isDriving:
            self.isDriving = False
            self.trip()
            return True
        else:
            return False

    def __str__(self):
        prompt = "The car is a " + self.make + " " + self.model
        prompt += " built in " + str(self.year) + " and weighs " + str(self.weight) + "kg."
        if self.NeedsMaintainance:
            prompt += "\nIt needs maintainance!\n"
        else:
            prompt += "\nIt does not need maintainance.\n"
        return prompt


class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False
    
    def Fly(self):
        if not self.isFlying:
            self.isFlying = True
            return True
        else:
            return False

    def Land(self): 
        if self.isFlying:
            self.isFlying = False
            self.trip()
            return True
        else:
            return False

    def __str__(self):
        prompt = "The plane is a " + self.make + " " + self.model
        prompt += " built in " + str(self.year) + " and weighs " + str(self.weight) + "kg."
        if self.NeedsMaintainance:
            prompt += "\nIt needs maintainance!\n"
        else:
            prompt += "\nIt does not need maintainance.\n"
        return prompt


#dataset
car1 = Cars("Toyota", "Corolla", 2000, 1500)
car2 = Cars("Honda", "Civic", 2010, 1750)
car3 = Cars("Mitsubishi", "Montero", 2020, 2000)
plane1 = Planes("Boeing", "747", 2002, 40000)

#simulation for TripsSinceMaintainance Counter
import random
print('Count simulator . . .')
for i in range(random.randrange(200)):
    car1.Drive()
    car1.Stop()
print('car1:', i)
for i in range(random.randrange(200)):
    car2.Drive()
    car2.Stop()
print('car2:', i)
for i in range(random.randrange(200)):
    car3.Drive()
    car3.Stop()
print('car3:', i)
for i in range(random.randrange(200)):
    plane1.Fly()
    plane1.Land()
print('plane1:', i)
print(". . . End\n")


print(car1)
print(car2)
print(car3)
print(plane1)
