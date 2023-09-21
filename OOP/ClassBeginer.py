
class SoftwareEngineer: # class

    company_name = "SOS"

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary



se1 = SoftwareEngineer("MAX",20,"Junior",5000) # Instance
se2 = SoftwareEngineer("JHON",30,"Expert",10000) # Instance

print(SoftwareEngineer.company_name)
print(se1.salary)
print(se2.name)