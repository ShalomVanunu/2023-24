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

    def __str__(self): # contrutor print string
        information = f" name ={self.name} , age = {self.age}"
        return information

    def __eq__(self, other):
        return other.age == self.age


se1 = SoftwareEngineer("MAX", 20, "Junior", 5000)  # Instance
se2 = SoftwareEngineer("JHON",20,"Expert",10000) # Instance

print(se1)
print(se1 == se2)