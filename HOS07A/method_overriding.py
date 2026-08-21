class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayData(self):
        print("In parent class displayData method")
        print(self.name)
        print(self.age)


class Employee(Person):
    def __init__(self, name, age, eid):
        # calling constructor of super class
        super().__init__(name, age)
        self.empid = eid

    def displayData(self):
        print("In child class displayData method")
        print(self.name)
        print(self.age)
        print(self.empid)


# Person class object
person = Person("John", 40)
person.displayData()

# Employee class object
emp = Employee("John", 40, "E005")
emp.displayData()