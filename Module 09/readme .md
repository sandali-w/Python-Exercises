# Fundamentals of object-oriented programming

## Exercise 1.py

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


# Main program
if __name__ == "__main__":
    new_car = Car("ABC-123", 142)

    print(f"Registration Number: {new_car.registration_number}")
    print(f"Maximum Speed: {new_car.maximum_speed} km/h")
    print(f"Current Speed: {new_car.current_speed} km/h")
    print(f"Travelled Distance: {new_car.travelled_distance} km")

## Exercise 2.py

class Car:
     def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

     def accelerate(self, speed_change):
        self.current_speed += speed_change

        # Ensure speed does not exceed maximum speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        # Ensure speed does not drop below zero
        if self.current_speed < 0:
            self.current_speed = 0


# Main program
if __name__ == "__main__":
    new_car = Car("ABC-123", 142)

    # Accelerations
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)

    print(f"Current speed after acceleration: {new_car.current_speed} km/h")

    # Emergency brake
    new_car.accelerate(-200)

    print(f"Final speed after emergency brake: {new_car.current_speed} km/h")

## Exercise 3.py

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


# Main program test matching exercise example
if __name__ == "__main__":
    new_car = Car("ABC-123", 142)
    new_car.travelled_distance = 2000
    new_car.current_speed = 60

    new_car.drive(1.5)

    print(f"New travelled distance: {new_car.travelled_distance} km")

## Exercise 4.py 

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


# Main race program
if __name__ == "__main__":
    cars = []

    # Create 10 cars with random maximum speeds between 100 km/h and 200 km/h
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        cars.append(Car(f"ABC-{i}", max_speed))

    race_finished = False

    # Simulation loop (hour by hour)
    while not race_finished:
        for car in cars:
            # Change speed randomly between -10 km/h and +15 km/h
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            # Drive for 1 hour
            car.drive(1)

            # Check if any car has reached 10,000 km
            if car.travelled_distance >= 10000:
                race_finished = True

    # Print results table
    print(
        f"{'Reg Num':<10} | {'Max Speed (km/h)':<18} | {'Current Speed (km/h)':<20} | {'Distance (km)':<15}"
    )
    print("-" * 72)
    for car in cars:
        print(
            f"{car.registration_number:<10} | {car.maximum_speed:<18} | {car.current_speed:<20} | {car.travelled_distance:<15.1f}"
        )