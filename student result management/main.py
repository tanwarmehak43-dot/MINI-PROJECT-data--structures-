students = {
    "Mehak": 85,
    "Riya": 92,
    "Aman": 78
}

total = sum(students.values())
average = total / len(students)

topper = max(students, key=students.get)

print("Student Marks:", students)
print("Average Marks:", average)
print("Topper:", topper, "-", students[topper])

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    else:
        grade = "C"

    print(name, "Grade:", grade)