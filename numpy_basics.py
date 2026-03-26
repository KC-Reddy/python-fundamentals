import numpy as np

# 1. Create a NumPy array of 5 student CGPAs
cgpas = np.array([6.8, 7.2, 8.5, 9.1, 7.9])
print("Student CGPAs:", cgpas)

# 2. Basic array operations
print("\n--- Basic Statistics ---")
print("Mean CGPA      :", np.mean(cgpas))
print("Max CGPA       :", np.max(cgpas))
print("Min CGPA       :", np.min(cgpas))
print("Std Deviation  :", round(np.std(cgpas), 4))

# 3. Math operations (applied to every element at once)
print("\n--- Math Operations ---")
print("CGPAs x 10     :", cgpas * 10)
print("CGPAs + 5      :", cgpas + 5)

# 4. Filtering: CGPAs above 7.5
print("\n--- Filtering: CGPAs above 7.5 ---")
above_75 = cgpas[cgpas > 7.5]
print("Filtered CGPAs :", above_75)

# 5. 2D array: 3 students x 3 exam scores
exam_scores = np.array([
    [85, 90, 78],   # Student 1
    [72, 68, 80],   # Student 2
    [91, 95, 88],   # Student 3
])

print("\n--- 2D Exam Scores Array ---")
print(exam_scores)

print("\n--- Shape Info ---")
print("Shape          :", exam_scores.shape)
print("Rows (students):", exam_scores.shape[0])
print("Cols (exams)   :", exam_scores.shape[1])
