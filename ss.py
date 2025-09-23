# ==============================
# Student Management System
# ==============================

# Student records will be stored in a list of dictionaries
students = []

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print("Student added successfully!\n")

# Function to display all students
def display_students():
    if len(students) == 0:
        print("No students found!\n")
    else:
        print("\n--- Student List ---")
        count = 1
        for student in students:
            print(count, ". Name:", student["name"], " Age:", student["age"], " Grade:", student["grade"])
            count += 1
        print()


# Function to search a student by name
def search_student():
    name = input("Enter name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found:", student)
            found = True
    if not found:
        print("Student not found!\n")

# Function to update a student's grade
def update_grade():
    name = input("Enter student name to update grade: ")
    for student in students:
        if student["name"].lower() == name.lower():
            new_grade = input("Enter new grade: ")
            student["grade"] = new_grade
            print("Grade updated!\n")
            return
    print("Student not found!\n")

# Function to delete a student
def delete_student():
    name = input("Enter student name to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted!\n")
            return
    print("Student not found!\n")

# Function to check statistics
def show_statistics():
    if not students:
        print("No data available!\n")
        return
    
    ages = [student["age"] for student in students]
    total = sum(ages)
    average = total / len(ages)
    print("\n--- Statistics ---")
    print("Total students:", len(students))
    print("Youngest age:", min(ages))
    print("Oldest age:", max(ages))
    print("Average age:", round(average, 2))
    print()

# ==============================
# Main Program (Menu-driven)
# ==============================

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Show Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add_student()
        case 2:
            display_students()
        case 3:
            search_student()
        case 4:
            update_grade()
        case 5:
            delete_student()
        case 6:
            show_statistics()
        case 7:
            print("Exiting program... Goodbye!")
            break
        case _:
            print("Invalid choice, please try again!\n")
