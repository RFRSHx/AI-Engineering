num_students = int(input("Enter the number of students: "))
students = {}

for i in range(num_students):
    name = input(f"\nEnter the name of student {i + 1}: ")
    grade = float(input(f"Enter the grade of {name}: "))
    students[name] = grade

for index, (student, grade) in enumerate(students.items(), start=1):
    print(f"{index}. {student} - {grade}")

average_grade = sum(students.values()) / num_students
print(f"\nThe average grade of the class is: {average_grade:.2f}")

highest_grade = max(students.values())

for student in students:
    if students[student] == highest_grade:
        print(f"\nThe student with the highest grade is: {student} - {highest_grade}")
        break

lowest_grade = min(students.values())

for student in students:
    if students[student] == lowest_grade:
        print(f"\nThe student with the lowest grade is: {student} - {lowest_grade}")
        break
