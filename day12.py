import matplotlib.pyplot as plt
import numpy as np

students = ["AMIT", "RIYA", "JOHN"]
math_marks = [85, 92, 78]
science_marks = [88, 95, 80]
english_marks = [82, 90, 76]
plt.figure(figsize=(6,5))
plt.bar(students, math_marks)
plt.title("Student Marks in Math")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
x = np.arange(len(students))
width = 0.25
plt.figure(figsize=(8,5))
plt.bar(x - width, math_marks, width, label="Math")
plt.bar(x, science_marks, width, label="Science")
plt.bar(x + width, english_marks, width, label="English")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Dashboard")
plt.xticks(x, students)
plt.legend()
plt.show()
