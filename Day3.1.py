#Write a function student_info() that:
#Takes name, marks in 3 subjects
#Returns average and grade:
#A: >=90
#B: >=75 and <90
#C: >=60 and <75
#D: <60



def student_info():
    name = str(input("Enter the name = "))
    marks1 = float(input("Enter the marks of subject 1 = "))
    marks2 = float(input("Enter the marks of subject 2 = "))
    marks3 = float(input("Enter the marks of subject 3 = "))

    avg_marks = (marks1 + marks2 + marks3)/3

    if avg_marks >= 90:
        Grade = "A"
    elif avg_marks >= 75:
        Grade = "B"
    elif avg_marks >= 60:
        Grade = "C"
    else:
        Grade = "D"

    return(avg_marks, Grade)

avg_marks, Grade = student_info()
print("Average Marsk =", avg_marks)
print("Grade =", Grade)

