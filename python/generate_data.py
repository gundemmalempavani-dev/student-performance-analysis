import csv
import random

departments = ["CSE", "ECE", "EEE", "MECH", "CIVIL"]

with open("student_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Student_ID",
        "Department",
        "Year",
        "Attendance",
        "Internal_Marks",
        "Semester_Marks",
        "Backlogs",
        "Placement"
    ])

    for i in range(1, 501):

        department = random.choice(departments)
        year = random.randint(1, 4)

        attendance = random.randint(55, 98)
        internal_marks = random.randint(45, 95)

        # Marks are slightly influenced by attendance
        semester_marks = min(
            100,
            max(
                35,
                int(internal_marks * 0.6 + attendance * 0.3 + random.randint(-10, 10))
            )
        )

        # Higher marks generally mean fewer backlogs
        if semester_marks >= 80:
            backlogs = random.choice([0, 0, 0, 1])
        elif semester_marks >= 60:
            backlogs = random.choice([0, 1, 1, 2])
        else:
            backlogs = random.choice([1, 2, 2, 3])

        # Placement probability
        if semester_marks >= 75 and backlogs == 0:
            placement = random.choice(["Yes", "Yes", "Yes", "No"])
        else:
            placement = random.choice(["Yes", "No", "No", "No"])

        writer.writerow([
            f"S{i:03d}",
            department,
            year,
            attendance,
            internal_marks,
            semester_marks,
            backlogs,
            placement
        ])

print("500 student records created successfully!")
