class Vehicle:

    def __init__(self, name, color='silver'):
        self.name = name
        self.color = color


    def get_name(self):
        return self.name


    def get_color(self):
        return self.color

class Car(Vehicle):

    def get_color(self):
        self.color = 'black'
        return self.color

    def radio_model(self):
        self.radio = "Android"
        return self.radio

car = Vehicle("Audi")
print(car.get_color())
print(car.get_name())


car = Car("Audi")
print(car.get_name())
print(car.get_color())
print(car.radio_model())