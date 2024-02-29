class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    @staticmethod
    def calculate_area_static(radius):
        return 3.14 * radius ** 2


if __name__ == '__main__':
    circle = Circle(radius=10)

    print("Calculating Area without static method")
    print(circle.area())
    print("-" * 30)
    print("Calculating Area with static method")
    print(Circle.calculate_area_static(10))
    print("-" * 30)
