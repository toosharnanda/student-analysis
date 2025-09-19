import pandas as pd
from sqlalchemy import create_engine

# Step 1: Connect to MySQL
engine = create_engine("mysql+mysqlconnector://root:root@localhost/studentdb")
print(engine)


# Step 2: Load table into Pandas
try:
    df = pd.read_sql("SELECT * FROM students", engine)
    print("✅ Data loaded successfully!\n")
    print(df, "\n")   # show all data
except Exception as e:
    print("⚠️ Error:", e)

# Step 3: Basic Analysis
if not df.empty:
    print("📊 Basic Analysis:\n")

    # Average marks
    avg_marks = df["marks"].mean()
    print(f"👉 Average Marks: {avg_marks:.2f}")

    # Highest scorer
    topper = df['marks'].idxmax()
    topper = df.loc[df["marks"].idxmax()]
    print(f"👉 Topper: {topper['name']} with {topper['marks']} marks")

    # Lowest scorer
    low = df.loc[df["marks"].idxmin()]
    print(f"👉 Lowest Scorer: {low['name']} with {low['marks']} marks")

    # Count of students
    print(f"👉 Total Students: {len(df)}")

import pandas as pd
from sqlalchemy import create_engine

# Step 1: Connect
engine = create_engine("mysql+mysqlconnector://root:root@localhost/studentdb")

# Step 2: Load both tables
students_df = pd.read_sql("SELECT * FROM students", engine)
attendance_df = pd.read_sql("SELECT * FROM attendance", engine)

print("✅ Data loaded successfully!\n")
print("Students Table:\n", students_df, "\n")
print("Attendance Table:\n", attendance_df, "\n")

# Step 3: Join tables
merged_df = pd.merge(students_df, attendance_df, left_on="id", right_on="student_id")

# Step 4: Calculate attendance percentage
merged_df["attendance_percent"] = (merged_df["attended_classes"] / merged_df["total_classes"]) * 100
print("📊 Merged Data with Attendance %:\n", merged_df, "\n")

# Step 5: Analysis
print("👉 Average Marks:", merged_df["marks"].mean())
print("👉 Average Attendance %:", merged_df["attendance_percent"].mean())

topper = merged_df.loc[merged_df["marks"].idxmax()]
print(f"👉 Topper: {topper['name']} with {topper['marks']} marks")

best_attendance = merged_df.loc[merged_df["attendance_percent"].idxmax()]
print(f"👉 Best Attendance: {best_attendance['name']} with {best_attendance['attendance_percent']:.2f}%")

