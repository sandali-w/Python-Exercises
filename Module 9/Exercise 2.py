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