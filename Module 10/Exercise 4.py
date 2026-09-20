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