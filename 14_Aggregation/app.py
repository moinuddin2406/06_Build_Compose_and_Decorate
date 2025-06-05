# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self ,name):
        self.name = name

class Department:
    def __init__(self ,employee):
        self.employee = employee

    def show_emploee(self):
        print(f"Employee in department: {self.employee.name}") 
if __name__ == "__main__":
    emp = Employee("Moin")  
    dep = Department(emp)
    dep.show_emploee()


        