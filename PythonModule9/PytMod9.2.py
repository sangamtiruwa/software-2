class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.maximum_speed))

new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print("Current speed after Acceleration:", new_car.current_speed, "km/h")

new_car.accelerate(-200)

print("Final speed after Emergency Break:", new_car.current_speed, "km/h")