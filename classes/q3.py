class Car():

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = 19
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        print("The car is stop.")


car = Car('honda', '3X', 2023)

print(car.fill_tank())