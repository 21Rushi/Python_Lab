student = {}

while True:
    print(
        "\n 1. Add Student"
        "\n 2. Update Grade"
        "\n 3. Print all Grades"
        "\n 4. Exit"
    )

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input; please enter a number.")
        continue

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student[name] = grade
        print("Student added successfully.")
    elif choice == 2:
        name = input("Enter student name to update grade: ")
        if name in student:
            grade = input("Enter new grade: ")
            student[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")
    elif choice == 3:
        print("Student Grades:")
        for name, grade in student.items():
            print(f"{name}: {grade}")
    elif choice == 4:
        print("Exiting.")
        break
    else:
        print("Invalid choice; please select 1-4.")