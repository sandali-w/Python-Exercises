# Inheritance

## Exercise 1.py

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}\n")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}\n")

# Main Program
if __name__ == "__main__":
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    magazine.print_information()
    book.print_information()

# Exercise 3.py

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.odometer = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.odometer += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kWh

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters

# Main Program
if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Select speed for both cars
    electric_car.accelerate(120)
    gasoline_car.accelerate(100)

    # Drive for three hours
    electric_car.drive(3)
    gasoline_car.drive(3)

    # Print odometer values
    print(f"Electric Car ({electric_car.registration_number}) Odometer: {electric_car.odometer} km")
    print(f"Gasoline Car ({gasoline_car.registration_number}) Odometer: {gasoline_car.odometer} km")