#M3Lab.py
#Tyler Bischoff
#Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
#The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes above.
#The app will then output the data in an easy-to-read and understandable format

#Class initilizations
class Vehicle():
    pass
    
class Automobile(Vehicle):
    pass
    
#Class instances
car1 = Automobile()
car1.type = "car"

#Input
print("""Hello welcome to the Vehicle Search Engine.
You have selected car.""")
car1.year = input("Enter the year: ")
car1.make = input("Enter the make: ")
car1.model = input("Enter the model: ")
car1.doors = input("Enter the the number of doors (2 or 4): ")
car1.roof = input("Enter the type of roof (solid or sun roof): ")

#Output
print("Here is the vehicle you entered.")
print(f"Vehicle type: {car1.type}")
print(f"Year: {car1.year}")
print(f"Make: {car1.make}")
print(f"Model: {car1.model}")
print(f"Number of doors: {car1.doors}")
print(f"Type of roof: {car1.roof}")