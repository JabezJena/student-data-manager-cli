# 📚 Student Data List Management System
# Hello World I am Jabez Jesudason Jena 

stds_list = []
stds_mark = []

def show_std_list(names, marks):
    if not names:
        print("No students in the list.")
    else:
        for i in range(len(names)):
            print("Student name:", names[i], "\tMark:", marks[i])

def add_std_list(names, marks):
    name = input("Enter the student name: ")
    mark = input("Enter student mark: ")
    names.append(name)
    marks.append(mark)

op = 'y'

while op.lower() == 'y':
    print("\n🎓 Welcome to the Student Management System 🎓")
    print("1. Show the Student List")
    print("2. Add a Student")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        show_std_list(stds_list, stds_mark)
    elif choice == 2:
        add_std_list(stds_list, stds_mark)
    else:
        print("Please select a valid option (1 or 2).")

    op = input("Do you want to continue? (y/n): ")

print("👋 Thank you for using the Student Management System!")
