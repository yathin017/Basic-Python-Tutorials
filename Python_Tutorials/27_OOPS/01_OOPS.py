class Data:

    increment = 1.5
    no_of_users = 0
    def __init__(self, fname, lname, salary, occupation = None):
        self.firstname=fname
        self.lastname=lname
        self.salary=salary
        self.occupation=occupation
        Data.no_of_users +=1

    def isAChild(self):
        if(self.occupation != None):
            print(f"No, {self.firstname} {self.lastname} is not a Child")
        else:
            print(f"Yes, {self.firstname} {self.lastname} is a Child")

    def isAStudent(self):
        if(self.occupation.lower() == "student"):
            print(f"Yes, {self.firstname} {self.lastname} is a Student")
        else:
            print(f"No, {self.firstname} {self.lastname} is not a Student")

    def increase(self):
        self.salary=int(self.salary*Data.increment)
    
harry= Data("Harry", "Jackson", 45000, "Software Engineer")
rohan= Data("Rohan", "Das", "Nil", "Student")
rahul= Data("Rahul", "Kumar", "Nil")

print("Number of Users:")
print(Data.no_of_users)

print("Salary:")
print(harry.salary)
print(rohan.salary)
print(rahul.salary)

print("Is a Student?")
harry.isAStudent()
rohan.isAStudent()

print("Is a Child?")
harry.isAChild()
rohan.isAChild()
rahul.isAChild()

print(harry.__dict__)
print(rohan.__dict__)
print(rahul.__dict__)

print("Increment")
print(harry.salary)
harry.increase()
print(harry.salary)

