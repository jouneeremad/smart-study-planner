from datetime import datetime

subjects = []
exams = {}

# Load subjects
try:
    with open("subjects.txt", "r") as file:
        for line in file:
            subjects.append(line.strip())
except FileNotFoundError:
    pass

# Load exams
try:
    with open("exams.txt", "r") as file:
        for line in file:
            subject, date = line.strip().split(",")
            exams[subject] = date
except FileNotFoundError:
    pass

while True:
    print("\n===== Smart Study Planner =====")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Add Exam")
    print("4. View Exams")
    print("5. Generate Study Plan")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        subject = input("Enter subject name: ")
        subjects.append(subject)

        with open("subjects.txt", "a") as file:
            file.write(subject + "\n")

        print("Subject added successfully!")

    elif choice == "2":
        print("\nSubjects:")

        if not subjects:
            print("No subjects found.")
        else:
            for subject in subjects:
                print("-", subject)

    elif choice == "3":
        subject = input("Enter subject name: ")

        if subject not in subjects:
            print("Subject not found!")
            continue

        exam_date = input("Enter exam date (YYYY-MM-DD): ")

        exams[subject] = exam_date

        with open("exams.txt", "a") as file:
            file.write(f"{subject},{exam_date}\n")

        print("Exam added successfully!")

    elif choice == "4":
        print("\nUpcoming Exams:")

        if not exams:
            print("No exams added.")
        else:
            today = datetime.today()

            for subject, exam_date in exams.items():
                exam_datetime = datetime.strptime(
                    exam_date, "%Y-%m-%d"
                )
                days_left = (exam_datetime - today).days

                print(f"\nSubject: {subject}")
                print(f"Exam Date: {exam_date}")
                print(f"Days Left: {days_left}")

    elif choice == "5":
        print("\n===== Study Plan =====")

        if not exams:
            print("Please add exams first.")
        else:
            today = datetime.today()

            for subject, exam_date in exams.items():
                exam_datetime = datetime.strptime(
                    exam_date, "%Y-%m-%d"
                )
                days_left = (exam_datetime - today).days

                if days_left > 0:
                    print(
                        f"Study {subject} for at least 1 hour daily "
                        f"for the next {days_left} days."
                    )
                else:
                    print(
                        f"The exam for {subject} has already passed."
                    )

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
