# Task 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")


person_1 = Person("Kalosh", 29)
person_1.greet()

# Task 2


class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def greet(self):
        print(f"My name is {self.name}, a {self.age} years old {self.job}.")


emp_1 = Employee("Kali", 30, "Software Engineer")
# print(emp_1.name)
emp_1.greet()
