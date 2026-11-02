
# Student Marks Program

m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))

total = m1 + m2 + m3
percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"

print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)