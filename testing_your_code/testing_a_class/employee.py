class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee with first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.annual_salary += amount
        
#Example usage
employee = Employee("John", "Doe", 50000)
print(employee.annual_salary)  # Output: 50000
employee.give_raise() # gives default raise of $5000
print(employee.annual_salary)  # Output: 55000
employee.give_raise(10000)
print(employee.annual_salary)  # Output: 65000