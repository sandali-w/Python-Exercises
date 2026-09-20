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