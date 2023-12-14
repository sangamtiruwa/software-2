class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor=0):
        self.current_floor = current_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Elevator is going up. {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Elevator going down. {self.current_floor}")

    def go_to_floor(self, to_floor):
        if self.current_floor < to_floor:
            for i in range(self.current_floor, to_floor):
                self.floor_up()
        if self.current_floor > to_floor:
            for i in range(self.current_floor, to_floor, -1):
                self.floor_down()
        print(f"Thank you for using the elevator. The current floor is {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number]
        print(f"Running elevator {elevator_number + 1} to floor {destination_floor}")
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm activated! Moving all elevators to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


building = Building(bottom_floor=0, top_floor=7, num_elevators=3)

building.run_elevator(elevator_number=0, destination_floor=3)
building.run_elevator(elevator_number=1, destination_floor=6)
building.run_elevator(elevator_number=2, destination_floor=2)

building.fire_alarm()