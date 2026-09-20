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