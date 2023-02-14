class Car:
    def __init__(self, make, model, year, price, used, mileage, doors, available):
        self.make = make
        self.model = model 
        self.year = year
        self.price = price
        self.used = used
        self.mileage = mileage 
        self.doors = doors
        self.available = available
        
    def __str__(self):
        return f'This car is a {self.year} {self.make} {self.model}'
    def nMileage(self):
        newMileage = input("What is the new mileage of this car?")
        self.mileage = newMileage
        return f'The new mileage of this car is {self.mileage}'
    
    def changeAvailability(self):
        if self.available == "False":
            x.available == "True"
            response = f'{x.model} is now available!'
        else: 
            x.available == "False"
            response = f"{x.model} is now unavailable!"
        return response

            


while True:
    file = open("cars.txt")
    cars = []
    properties = []
    while True:
        line = file.readline()
        if not line: 
            break
        crystal = line.replace('\n',"")
        cry = crystal.split(": ")
        if len(cry) == 2:
            properties.append(cry[1])
        else: 
            cars.append(Car(*properties))
            properties = []

    file.close()
    selection = int(input("Select one of the options:\n1. Find a Car (Using the model)\n2. Add a car\n3.Change the availability of a car\n4. Change Mileage of a car\n"))
    if selection == 1: 
        search = input("What model of car are you looking for? ")
        for x in cars: 
            if x.model == search:
                print(x)

    elif selection == 2: 
        newFile = open("cars.txt",'a')
        newMake = input("What is the make of your car? ")
        newModel = input("What is the model of your car?")
        newYear = input("What is the year of your car? ")
        newPrice = input("What is the price of your car? ")
        newUsed = input("Is your car used? True or False")
        newMileage = input("What is the mileage on your car? ")
        newDoors = input("How many doors does your car have")

        newFile.write("\nMake: " + newMake + "\n" + "Model: " + newModel + "\n" + "Year: " + newYear + "\n" + "Price: " + newPrice + "\n" + "Used: " + newUsed + "\n" +  "Mileage: " + newMileage + "\n" + "Doors: " + newDoors + "\nAvailable: TRUE" + "\n")
        newFile.close()
    elif selection == 3:
        soldCar = input("What car model would you like to sell?")
        for x in cars:
            if x.model == soldCar:
                print(x.changeAvailability())

    elif selection == 4:
        changeCar = input("What car would you like to change the mileage of? ")
        for x in cars:
            if x.model == changeCar:
                print(x.nMileage())


