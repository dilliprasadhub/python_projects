student_grades = {
    "Alice": [85, 90, 78, 92],
    "Bob": [76, 88, 95],
    "Charlie": [82, 89, 75, 81, 90],
    "David": [92, 95, 88]
}

average_grades = {}

for student, grades in student_grades.items():
    
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    
    
    average_grades[student] = round(average, 2)


print("Original grades dictionary:")
for student, grades in student_grades.items():
    print(f"{student}: {grades}")