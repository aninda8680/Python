#Condiitonal Statements (if/else)

age = int(input("Enter the age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a child")



#Nested if/else Statements

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("You are just pased")
else:
    print("FAILED")

