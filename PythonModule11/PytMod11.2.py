class Car:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        pass

class ElectricCar(Car):
    def __init__(self, name, maximum_speed, battery_capacity):
        super().__init__(name)
        self.maximum_speed = maximum_speed
        self.battery_capacity = battery_capacity

    def print_information(self):
        print("Electric Car Information")
        print(f"Registration Number: ", self.name)
        print(f"Maximum speed: ", self.maximum_speed, "km/h")
        print(f"Battery Capacity: ", self.battery_capacity, "kWh")

class GasolineCar(Car):
    def __init__(self, name, maximum_speed, volume):
        self.name = name
        self.maximum_speed = maximum_speed
        self.volume = volume

    def print_information(self):
        print("Gasoline Car Information")
        print("Registration Number: ", self.name)
        print("Maximum Speed: ", self.maximum_speed, "km/h")
        print("Volume: ", self.volume, "L")

electric_car = ElectricCar("ABC-15", 180,52.5)
gasoline_car = GasolineCar("ACD_123", 165,  32.3)

electric_car.print_information()
print("\n")
gasoline_car.print_information()
