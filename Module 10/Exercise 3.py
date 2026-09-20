class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [
            Elevator(bottom_floor, top_floor) for _ in range(num_elevators)
        ]

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\n--- Operating Elevator {elevator_number} ---")
        self.elevators[elevator_number - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\n*** FIRE ALARM ACTIVATED! ALL ELEVATORS RETURNING TO BOTTOM FLOOR ***")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"\nMoving Elevator {i} to bottom floor:")
            elevator.go_to_floor(self.bottom_floor)


# Main program test
if __name__ == "__main__":
    building = Building(1, 10, 3)

    # Move elevators up first
    building.run_elevator(1, 7)
    building.run_elevator(2, 4)
    building.run_elevator(3, 9)

    # Fire alarm test
    building.fire_alarm()