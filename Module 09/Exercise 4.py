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