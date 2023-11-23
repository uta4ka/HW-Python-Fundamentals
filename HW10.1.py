#Task1

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init(4)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
#Task2

class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return f"I am a species of '{cls.species}'."

    @staticmethod
    def get_message():
        return "This is a static message."
    

#Task3
class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_total_employees(self):
        return f"Total number of employees: {Employee.total_employees}"

    def display_employee_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"