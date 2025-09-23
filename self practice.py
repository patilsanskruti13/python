students=[]
# Function to add a student
def add_student():
    name=input("enter student name :")
    grade=input("enter grade :")
    age=input("enter age :")
    
    student={"name":name,"grade":grade,"age":age}
    students.append(student)
    print(" added successfully")
    
# Function to display all student    
def display_students():
    if len(students)==0:
        print("no student data")
    else:
        print("\n--- Student List ---")
        count = 1
        for student in students:
            print(count,". Name:",student["name"],"Grade:",student["grade"],"Age:",student["age"])
            count+=1
        print()

# Function to search a student by name
def search_student():
    name=input("enter the student name to search")
    found = False
    for student in students:
        if student["name"].lower==name.lower:
            print("Student found:", student)
            found = True
    if not found:
        print("Student not found!\n")        
        
def update_grade():
    name=input("enter student name  to update data:")
    for student in students:
        if student["name"].lower()==name.lower():
            new_grade=input("enter new grade:")
            student["grade"]=new_grade
            print("updated successfully")
            return 
    print("no student found")   
def delete_student():
    name=input("enter student name to delete :")
    for student in students:
        if student["name"].lower()==name.lower():
            students.remove(student)
            print("Student deleted!\n")
            return
    print("student not found") 
     
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
        
