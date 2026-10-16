# employee_directory_haider_jareer.py
import json

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name
        }

    def get_info(self):
        return f"ID: {self.emp_id} - Name: {self.name}"

class EmployeeDirectory:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = []

    def add_employee(self, emp_id, name):
        # Prevent duplicate IDs in memory
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return
        new_emp = Employee(emp_id, name)
        self.employees.append(new_emp)

    def display_directory(self):
        if not self.employees:
            print("Directory is empty.")
            return
        for emp in self.employees:
            print(emp.get_info())

    def save_data(self):
        data = [emp.to_dict() for emp in self.employees]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

# Execution block
if __name__ == "__main__":
    directory = EmployeeDirectory()
    
    # Add your 4 clean employees
    directory.add_employee(369, "Jareer Haider")
    directory.add_employee(666, "Dean Winchester")
    directory.add_employee(1000, "Ryomen Sukuna")
    directory.add_employee(777, "Satoru Gojo")
    
    print("--- Clean Employee Directory ---")
    directory.display_directory()
    directory.save_data()
