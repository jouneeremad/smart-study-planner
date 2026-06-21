subjects = []

try:
    with open("subjects.txt", "r") as file:
        for line in file:
            subjects.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\nSmart Study Planner")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        subject = input("Enter subject name: ")
        subjects.append(subject)

        with open("subjects.txt", "a") as file:
            file.write(subject + "\n")

        print("Subject added!")

    elif choice == "2":
        print("\nYour Subjects:")
        for s in subjects:
            print("-", s)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
