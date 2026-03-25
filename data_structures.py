student_names = ["Krishna", "Arjun", "Priya", "Sneha", "Rahul"]
student_cgpas = [7.15, 8.20, 7.80, 6.90, 9.10]

student_profile = {
    "name": "Krishna Chaitanya Reddy Kothakapu",
    "age": 22,
    "city": "Mahabubnagar",
    "university": "University of Pittsburgh",
    "cgpa": 7.15,
    "skills": ["Python", "Machine Learning", "Data Analysis", "SQL"]
}

print("=" * 35)
print("      STUDENT CGPA LIST")
print("=" * 35)
for name, cgpa in zip(student_names, student_cgpas):
    print(f"{name:<10} : {cgpa}")
print("=" * 35)


def get_top_students(names, cgpas, threshold=7.5):
    return [(name, cgpa) for name, cgpa in zip(names, cgpas) if cgpa > threshold]


print("\nTop Students (CGPA > 7.5):")
print("-" * 35)
top_students = get_top_students(student_names, student_cgpas)
for name, cgpa in top_students:
    print(f"{name:<10} : {cgpa}")
