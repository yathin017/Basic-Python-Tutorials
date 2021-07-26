class Employee:
    increment = 1.5
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employees +=1

    def increase(self):
        self.salary = int(self.salary*self.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

harry = Employee('Harry','Jackson',44000)  
rohan = Employee('Rohan','Das',50000)
print(Employee.no_of_employees)

print(harry.salary)
Employee.change_increment(2)
harry.increase()
print(harry.salary)