#Creating a class
class Vehicle:
    #Creating a class attribute
    class_attribute = "This is a vehicle"
    #Creating a constructor
    def __init__(self,name,color):
        self.name = name
        self.color = color

    #Instance method
    def display_info(self):
        print(f"Name: {self.name}, Color: {self.color}")

    #Class method
    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"I can make this access the class attribute: {Vehicle.class_attribute}")

    #Static Method
    @staticmethod
    def static_method():
        print("I am a static method, I cannot access anything")

class Car(Vehicle):
    def __init__(self,name,color,fuel_type):
        super().__init__(name,color)
        self.fuel_type = fuel_type

    #Method overriding
    def display_info(self):
        print(f"{self.name}, {self.color}, {self.fuel_type}")

#Creating an object
vehicle = Vehicle("Cool Car", "Red")
vehicle.display_info()

car = Car("Luxury Car", "Black", "Petrol")
car.display_info()

Vehicle.class_method()
Vehicle.static_method()
