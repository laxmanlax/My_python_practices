## Python Object_oriented Programming
class Employee:
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@comp.com'
    
    def fullName(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)




##########
emp1 = Employee("laxman", "Goswami", 200000000000000)
emp1 = Employee("Rd", "Goswami", 24000000000000)


print Employee
# print emp1.first , emp1.pay 
# 
# #########
# 
# emp1.apply_raise()
# print emp1.first , emp1.pay 
# 
# #########
# print Employee.fullName(emp1)
# print emp1.fullName()