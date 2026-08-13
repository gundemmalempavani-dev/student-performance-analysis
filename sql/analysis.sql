-- ==========================================
-- Student Performance Analysis
-- SQL Analysis
-- ==========================================

-- 1. Total number of students
SELECT COUNT(*) AS Total_Students
FROM students;


-- 2. Number of students in each department
SELECT
    Department,
    COUNT(*) AS Student_Count
FROM students
GROUP BY Department;


-- 3. Average semester marks by department
SELECT
    Department,
    ROUND(AVG(Semester_Marks), 2) AS Average_Marks
FROM students
GROUP BY Department
ORDER BY Average_Marks DESC;


-- 4. Average attendance by department
SELECT
    Department,
    ROUND(AVG(Attendance), 2) AS Average_Attendance
FROM students
GROUP BY Department
ORDER BY Average_Attendance DESC;


-- 5. Students with attendance below 75%
SELECT
    Student_ID,
    Department,
    Attendance
FROM students
WHERE Attendance < 75
ORDER BY Attendance ASC;


-- 6. Total backlogs by department
SELECT
    Department,
    SUM(Backlogs) AS Total_Backlogs
FROM students
GROUP BY Department
ORDER BY Total_Backlogs DESC;


-- 7. Placement count
SELECT
    Placement,
    COUNT(*) AS Student_Count
FROM students
GROUP BY Placement;


-- 8. Placement analysis by department
SELECT
    Department,
    COUNT(*) AS Total_Students,
    SUM(
        CASE
            WHEN Placement = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Placed_Students
FROM students
GROUP BY Department;
