import random

class Car:
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.maximum_speed = random.randint(100, 200)
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.maximum_speed))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = [Car(f"ABC-{i}") for i in range(1, 11)]

while all(car.travelled_distance < 10000 for car in cars):
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

print("{:<12} {:<15} {:<15} {:<20}".format("Registration", "Max Speed (km/h)", "Current Speed (km/h)", "Travelled Distance (km)"))
print("-" * 62)
for car in cars:
    print("{:<12} {:<15} {:<15} {:<20}".format(car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance))
