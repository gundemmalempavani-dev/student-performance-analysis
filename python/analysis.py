import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the student dataset
df = pd.read_csv("../data/student_data.csv")

# Display first 5 rows
print("First 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Average marks by department
avg_marks = df.groupby("Department")["Semester_Marks"].mean()

print("\nAverage Semester Marks by Department:")
print(avg_marks)

# Average attendance by department
avg_attendance = df.groupby("Department")["Attendance"].mean()

print("\nAverage Attendance by Department:")
print(avg_attendance)

# Total backlogs by department
total_backlogs = df.groupby("Department")["Backlogs"].sum()

print("\nTotal Backlogs by Department:")
print(total_backlogs)

# Placement count
placement_count = df["Placement"].value_counts()

print("\nPlacement Count:")
print(placement_count)

# Attendance and marks correlation
correlation = df["Attendance"].corr(df["Semester_Marks"])

print("\nAttendance vs Semester Marks Correlation:")
print(round(correlation, 2))


# -------------------------------
# Chart 1: Average Marks
# -------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Department",
    y="Semester_Marks"
)

plt.title("Average Semester Marks by Department")
plt.xlabel("Department")
plt.ylabel("Semester Marks")

plt.tight_layout()
plt.show()


# -------------------------------
# Chart 2: Attendance vs Marks
# -------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Semester_Marks",
    hue="Department"
)

plt.title("Attendance vs Semester Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Semester Marks")

plt.tight_layout()
plt.show()


# -------------------------------
# Chart 3: Backlogs
# -------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    x=total_backlogs.index,
    y=total_backlogs.values
)

plt.title("Total Backlogs by Department")
plt.xlabel("Department")
plt.ylabel("Total Backlogs")

plt.tight_layout()
plt.show()
