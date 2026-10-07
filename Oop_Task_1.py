class Employee:
    def __init__(self,name,employee_id,salary):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary

    def display_details(self):
        print("Name:",self.name)
        print("ID:",self.employee_id)
        print("salary:",self.salary)
    def increase_salary(self,percentage):
        increase=self.salary * percentage/100
        self.salary=self.salary+increase


employee=Employee("Arun",102,30000)
employee.display_details()
employee.increase_salary(15)
employee.display_details()