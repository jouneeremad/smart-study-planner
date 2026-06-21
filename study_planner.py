subjects = []

while True:
    print("\nSmart Study Planner")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        subject = input("Enter subject name: ")
        subjects.append(subject)
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
