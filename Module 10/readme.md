# Association

## Exercise 1.py

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
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Invalid floor requested.")
            return

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()
# Main program test
if __name__ == "__main__":
    h = Elevator(1, 5)

    print("Moving to 5th floor:")
    h.go_to_floor(5)

    print("\nMoving back to bottom floor:")
    h.go_to_floor(1)

## Exercise 2.py

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

## Exercise 3.py 

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

## Exrcise 4.py

import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'='*25} {self.name} Status {'='*25}")
        print(
            f"{'Reg Num':<10} | {'Max Speed':<12} | {'Current Speed':<15} | {'Distance':<15}"
        )
        print("-" * 65)
        for car in self.cars:
            print(
                f"{car.registration_number:<10} | {car.maximum_speed:<12} km/h | {car.current_speed:<15} km/h | {car.travelled_distance:<15.1f} km"
            )

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# Main race program
if __name__ == "__main__":
    # Create 10 cars
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        cars.append(Car(f"ABC-{i}", max_speed))

    # Create the race
    derby = Race("Grand Demolition Derby", 8000, cars)

    hours_elapsed = 0

    # Race loop
    while not derby.race_finished():
        derby.hour_passes()
        hours_elapsed += 1

        # Print status every 10 hours
        if hours_elapsed % 10 == 0:
            derby.print_status()

    # Final status after race finishes
    print(f"\nRace completed in {hours_elapsed} hours!")
    derby.print_status()