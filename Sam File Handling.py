students = {}


def add_student():
    studentID = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))

    grades = []
    while True:
        grade = input("Enter grade (type 'done' to finish): ")
        if grade.lower() == "done":
            break
        try:
            grades.append(float(grade))
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")
    students[studentID] = {
        "name": name,
        "age": age,
        "grades": grades
    }
    print(f"\n Student {name} added successfully!!\n")


def update_student():
    studentID = input("Enter Student ID to update: ")

    if studentID in students:
        print(f"\nCurrent Info: {students[studentID]}")
        choice = input(
            "What do you want to update?? ( name / age / grades ): ").lower()
        if choice == "name":
            new_name = input("Enter new name:")
            students[studentID]["name"] = new_name

        elif choice == "age":
            new_age = int(input("Enter new age:"))
            students[studentID]["age"] = new_age

        elif choice == "grades":
            print("Re-enter grades (type 'done' to finish):")
            new_grades = []
            while True:
                grade = input("Enter grade (or type 'done' to finish): ")
                if grade.lower() == "done":
                    break
                try:
                    new_grades.append(float(grade))
                except ValueError:
                    print(" Please enter a valid number or 'done' to finish.")
            students[studentID]["grades"] = new_grades
            if new_grades:
                print("First two grades (slicing):", new_grades[:2])
                print("Deleting last grade...")
                del new_grades[-1]
                print("Grades after deletion:", new_grades)

        else:
            print("Invalid option")
        print(f"\n Student {studentID} updated successfully!\n")

    else:
        print("Student ID not found :((\n")


def delete_student():
    studentID = input("Enter Student ID to update: ")
    if studentID in students:
        confirm = input(
            f"are you sure you want to delete {students[studentID]['name']}?? yes/no: ").lower()
        if confirm == "yes":
            del students[studentID]
            print(f"Student{studentID} deleted successfully!!\n")
        else:
            print("Cancelled.\n")
    else:
        print("Student ID not found.\n")


def display_students():
    if not students:
        print("\n No students found!! ")
        return

    print("\n===== Student Records =====")
    for studentID, info in students.items():
        print(f"\n Student ID: {studentID}")
        print(f"\n Name: {info['name']}")
        print(f"\n Age: {info['age']}")
        print(f"\n Grades: ", end=" ")

        for g in info["grades"]:
            if g < 50:
                continue
            print(g, end=" ")
        print()


def save_to_file(filename="student.csv"):
    with open(filename, "w") as pen:
        for studentID, info in students.items():
            grades_str = ";".join(map(str, info["grades"]))
            line = f"{studentID},{info['name']},{info['age']},{grades_str}\n"
            pen.write(line)
    print(f"\n Data saved to {filename}")


def load_from_file(filename="student.csv"):
    try:
        with open(filename, "r") as pen:
            for line in pen:
                line = line.strip()
                studentID, name, age, grades_str = line.split(",")
                grades = [float(g) for g in grades_str.split(";")if g]
                students[studentID] = {
                    "name": name,
                    "age": age,
                    "grades": grades
                }
        print(f"\n Data loaded from {filename}\n")
    except FileNotFoundError:
        print(f"\n no file found with the name {filename}. Starting fresh!!\n")


while True:
    choice = input(
        "===== Student Information System ====="
        "\n1. Add Student"
        "\n2. Display Students"
        "\n3. Update Student"
        "\n4. Delete Student"
        "\n5. Save to File"
        "\n6. Load from File"
        "\n7. Exit"
        "\nEnter your choice: ").upper()

    # CHOICES
    if choice in ["7", "EXIT"]:
        save_to_file()
        print("Thank you, Goodbye!!")
        break

    elif choice in ["1", "ADD STUDENT"]:
        print("Add a student")
        add_student()

    elif choice in ["2", "DISPLAY STUDENTS"]:
        print("Displaying students")
        display_students()

    elif choice in ["3", "UPDATE STUDENT"]:
        print("Update student")
        update_student()

    elif choice in ["4", "DELETE STUDENT"]:
        print("Delete student")
        delete_student()

    elif choice in ["5", "SAVE TO FILE"]:
        print("Save to file")
        save_to_file()

    elif choice in ["6", "LOAD FROM FILE"]:
        print("Load from file")
        load_from_file()

    else:
        print("Invalid input, Please try again")
