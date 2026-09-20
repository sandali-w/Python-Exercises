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
        # Elevator numbers are 1-indexed for the user, 0-indexed in list
        self.elevators[elevator_number - 1].go_to_floor(destination_floor)


# Main program test
if __name__ == "__main__":
    building = Building(1, 10, 3)

    building.run_elevator(1, 5)
    building.run_elevator(2, 8)
    building.run_elevator(3, 3)
