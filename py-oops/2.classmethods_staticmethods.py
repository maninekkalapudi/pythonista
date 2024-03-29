'''We'll learn about regular methods, class methods and static methods
video-> https://youtu.be/BJ-VvGyQxho
'''
import datetime
class Employee:

    # Class variables
    num_of_emps = 0 # Variable to count the no. of employees
    raise_amount = 1.04

    # '''__init__ is the constructor for the class and 
    # all the variables that the class takes can be initialized here
    def __init__(self, first, last, pay):
        # Instance variables initialized in the constructor
        self.first = first
        self.last = last
        self.email = first +'.'+ last +'@company.com'
        self.pay = pay
        
        # This variable doesn't need to 'self' as it belongs to the class and not any particular instance
        Employee.num_of_emps += 1

    # Class methods
    # if we forget 'self' parameter for methods it'll throw 
    # "<method_name> takes 0 positional arguments but 1 was given" error-> it's confusing
    # Regular method in a class takes self param by covention 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Class method to apply the raise   
    def apply_raise(self):
        #we can also use 'Employee.raise_amount' or 'self.raise_amount' but never only 'raise_amount'
        self.pay = self.pay * self.raise_amount 
    
    # This is using the decorators to declare classmethod
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


    '''Class methods as alternative constructors -> use these classmethods in order to 
    provide multiple ways of creating objects'''
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # cls is nothing but Employee
        return cls(first, last, pay)

    '''Source: https://www.journaldev.com/18722/python-static-method
    Static method -> Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class.
    This means that a static method can be called without an object for that class. This also means that static methods cannot modify the state of an object as they are not bound to it. Let’s see how we can create static methods in Python.
    
    Static method -> It has a logical connection to the class but doesn't depend on any specific instance of the class or class variable'''
    @staticmethod
    def is_workday(day):  #doesn't take an instance or a class as the first argument and we can pass any argument
        if (day.weekday() == 5) or (day.weekday()) == 6:
            return False
        else:
            return True

# Initializing Employee class with the suitable input values for the constructor
emp1 = Employee('Manikantha', 'Nekkalapudi', 50000);
emp2 = Employee('Test', 'User', 60000);

# Print Employee class raise_amount variable
print(Employee.raise_amount)

# Print emp1 instance/object raise_amount variable
print(emp1.raise_amount)

# Print emp2 instance/object raise_amount variable
print(emp2.raise_amount)

# Set raise_amount for the class using the set_raise_amt method
Employee.set_raise_amt(1.05)

print("="*50)
# All the raise_amount is set to 1.05
print(Employee.raise_amount)

# Print emp1 instance/object raise_amount variable after the class variable update
print(emp1.raise_amount)

# Print emp2 instance/object raise_amount variable after the class variable update
print(emp2.raise_amount)

# Even using this below line will change all the class variable value
emp1.set_raise_amt(1.05)

# Employee info in string with '-' separator
emp_str_1 = 'John-Doe-50000'
emp_str_2 = 'Corey-Schafer-60000'
emp_str_2 = 'Bruce-Wane-200000'

# calling from_string classmethod to get the Employee object
new_emp_1 = Employee.from_string(emp_str_1)

print("="*50)
my_date = datetime.date(2017, 10, 7)
print(Employee.is_workday(my_date))