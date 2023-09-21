class SoftwareEngineer:  # class

    company_name = "SOS"

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code")

    def eat(self, food):
        print(f"{self.name} is eating {food} for morning")

se1 = SoftwareEngineer("MAX",20,"Junior",5000) # Instance
se1.code()
se1.eat("egg")
se2 = SoftwareEngineer("JHON",30,"Expert",10000) # Instance
se2.code()