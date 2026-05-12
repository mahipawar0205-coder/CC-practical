# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    
    student = {
        "name": name,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        print("\nStudent Records:")
        for s in students:
            print("Name:", s["name"], "| Marks:", s["marks"])
        print()


def search_student():
    search_name = input("Enter student name to search: ")
    
    found = False
    
    for s in students:
        if s["name"].lower() == search_name.lower():
            print("Student Found!")
            print("Name:", s["name"])
            print("Marks:", s["marks"])
            found = True
            break
    
    if not found:
        print("Student not found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
        
    elif choice == "2":
        display_students()
        
    elif choice == "3":
        search_student()
        
    elif choice == "4":
        print("Program Ended")
        break
        
    else:
        print("Invalid Choice\n")
