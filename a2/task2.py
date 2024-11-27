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



emp = emp1.from_string("1,2")
