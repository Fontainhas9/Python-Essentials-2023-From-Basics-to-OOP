class Car:
    color = "red"  # class attribute (all cars will have same color)

# Use a constructor to allow instances to have their own attributes


class Dog:
    def __init__(self, name):  # Constructor
        self.name = name

    def bark(self):
        return "Woof!"


if __name__ == '__main__':
    my_car = Car()
    print(my_car.color)  # Outputs: white
    my_car2 = Car()
    print(my_car2.color)

    dog1 = Dog(name="Rocky")
    dog2 = Dog(name="Sandy")
    print(dog1.name, dog2.name)
    print(dog1.bark())
