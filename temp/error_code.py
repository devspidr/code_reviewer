import os,sys,math,json

class Employee:
    def __init__(self, name, age, salary, dept = "General"):
         self.name=name
         self.age = age
         self.salary= salary
         self.dept = dept
    def info(self):
        print("Employee:",self.name)
        print("Department:",self.dept)
        print("Age:",self.age)
        print("Salary:",self.salary)
    
    def promote(self,amount):
      self.salary = self.salary + amount
      print("New salary:", self.salary)
      if amount>5000:
        print("You got a big raise!")
      else:
        print("You got a small raise.")
        
def average_salary(emps):
     total = 0
     for emp in emps:
         total += emp.salary
     avg = total / len(emps)
     return avg
     
def find_oldest(emps):
    oldest = emps[0]
    for e in emps:
        if e.age > oldest.age:
            oldest = e
        else:
            continue
    print("Oldest Employee is",oldest.name, "aged", oldest.age)
    return oldest

def load_employees(file_path):
 try:
     with open(file_path,"r") as f:
         data = json.load(f)
         employees=[]
         for emp in data:
             employees.append(Employee(emp["name"],emp["age"],emp["salary"],emp["dept"]))
         return employees
 except Exception as e:
     print("Failed loading file",e)

def save_report(emps):
    report = {"total": len(emps), "avg_salary": average_salary(emps)}
    with open("report.json","w") as f:
         json.dump(report,f)
    print("Report saved.")
    return True

def main():
     path = "employees.json"
     employees = load_employees(path)
     if employees == None:
         print("No data loaded.")
     else:
         for e in employees:
              e.info()
              if e.salary < 40000:
                 e.promote(3000)
                 if e.dept == "Sales":
                       e.promote(2000)
     avg = average_salary(employees)
     print("Average salary is:",avg)
     find_oldest(employees)
     save_report(employees)
     print("DONE")

if __name__=="__main__":
 main()
