class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.maximum_speed))

    def drive(self, hours):
        self.travelled_distance += self.current_speed*hours

new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

new_car.drive(1.5)

print("Current Speed:", new_car.current_speed, "km/h")
print("Travelled Distance:", new_car.travelled_distance, "km")

