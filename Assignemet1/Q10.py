# Q10: Calculate average marks and display the grade

mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

if all(0 <= mark <= 100 for mark in (mark1, mark2, mark3)):
    average = (mark1 + mark2 + mark3) / 3
    print("Average marks =", round(average, 2))

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade =", grade)
else:
    print("Marks must be between 0 and 100.")
