class Employee:
    count = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def no_of_employees(cls):
        cls.count += 1
        return cls.count
    
    @classmethod
    def from_string(cls, string):
        a, b = map(int, string.split(","))
        emp = cls(a, b)
        return emp
    
emp1 = Employee(5, 6)
# emp2 = Employee()
# emp3 = Employee()
# emp4 = Employee()
# emp5 = Employee()
# emp6 = Employee()

print(Employee.no_of_employees())

emp = emp1.from_string("1,2")
print(emp)
print(emp1)