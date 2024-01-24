class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} | {self.name} | {self.age} | {self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        print("Employee ID | Name  | Age | Salary")
        print("-" * 40)
        for emp in self.employees:
            print(emp)

    def sort_table(self, key):
        self.employees.sort(key=lambda x: getattr(x, key))
        print(f"\nTable sorted by {key}:\n")
        self.display_table()


if __name__ == "__main__":
    # Creating Employee objects
    employee_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    # Creating EmployeeTable object
    emp_table = EmployeeTable(employee_data)

    # Displaying the original table
    print("Original Employee Table:\n")
    emp_table.display_table()

    print("\nSelect sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")

    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        emp_table.sort_table("age")
    elif choice == 2:
        emp_table.sort_table("name")
    elif choice == 3:
        emp_table.sort_table("salary")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    print("\nEmployee Table after Sorting:\n")
    emp_table.display_table()
