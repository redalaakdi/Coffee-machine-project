# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# But don't worry, I will explain how to do everything in the video tutorials on Udemy.


class Car:
    num_wheels = 4
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    def accelerate(self):
        print(f"the {self.color} is accelerating")

class ElectricCar(Car):
    def __init__(self, color, speed):
        super().__init__(color, speed)
        self.battery_level = 150
    def charge(self):
        print(f"Charging the {self.color} Tesla...")


my_tesla = ElectricCar("white", 250)
print(my_tesla.color)
print(my_tesla.battery_level)
my_tesla.accelerate()
my_tesla.charge()

my_car_1 = Car("red", 200)
my_car_1.num_wheels = 6
print(my_car_1.color)
print(my_car_1.speed)
my_car_1.accelerate()

my_car_2 = Car("blue", 220)
print(my_car_2.color)
print(my_car_2.speed)

print(my_car_1.num_wheels)
print(my_car_2.num_wheels)
print(Car.num_wheels)




