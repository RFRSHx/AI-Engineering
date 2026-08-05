employees = {}

num_employees = int(input("How many employees do you want to enter? "))

for _ in range(num_employees):
    name = input("\nWhat is their name? ")
    age = int(input(f"\nWhat is {name}'s age? "))
    department = input(f"\nWhat is {name}'s department? ")
    salary = int(input(f"\nWhat is {name}'s salary? "))

    employees[name] = {
        "age": age,
        "department": department,
        "salary": salary,
        "skills": [],
    }
    num_skills = int(input(f"\nHow many skills does {name} have?"))

    for _ in range(num_skills):
        skill = input("\nWhat are the skills? ")
        employees[name]["skills"].append(skill)
    
def print_employee(name):

    employee = employees[name]

    print("\n=====================")
    print("Employees' Directory")
    print("=====================\n")

    print("Name: ", name)
    print("Age: ", employee["age"])
    print("Department: ", employee["department"])
    print("Salary: ", employee["salary"])
    print("\nSkills: ")
    for skill in employee["skills"]:
        print(f"\n - {skill}")

for employee in employees:
    print_employee(employee)

search_query = input("\nWhich employee do you want to search for? ")

if search_query in employees:
    print_employee(search_query)
else:
    print("\nEmployee not found!")