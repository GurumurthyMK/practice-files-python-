class Company:
    class Employee:
            def __init__(self,name,position):
                self.name = name
                self.position = position

            def get_details(self):
                 return f"{self.name}, {self.position}"
            
            
    def __init__(self,company_name):
        self.company_name = company_name
        self.employees = []
    
    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employees.append(new_employee)

    def list_employees(self):
         return [employee.get_details() for employee in self.employees]
    
company = Company("Cybergrid")
company.add_employee("Guru", "Founder")
company.add_employee("Sharanya", "Co-Founder")
company.add_employee("Karthik", "Co-Organizer")
company.add_employee("XYZ","Co-Organizer")

for employee in company.list_employees():
     print(employee)