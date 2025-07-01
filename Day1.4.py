#✅ 10 Practice Questions
#1️⃣ Write a Python program to swap two numbers input by the user.

a = int(input("Enter the first number: " ))
b = int(input("Enter the second number: "))

c = a
a = b
b = c

print("a is: ", a)
print("b is: ", b)


#2️⃣ Create a variable x with value 10, and print its square.

x = 10
print(x*x)

#3️⃣ Take input of your first name and last name, and print them combined as full name.

fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
print(fname + " " + lname)

#4️⃣ Check if an input number is positive, negative, or zero.

x = int(input("Enter the number: "))

if x >= 1:
    print("Positive")
elif x == 0:
    print("Zero")
else :
    print("Negative")

#5️⃣ Compute the remainder when one number is divided by another (using %).

x = int(input("Enter the first Number: "))
y = int(input("Enter the second Number: "))

print(x % y)

#6️⃣ Write a program to calculate the area of a circle given the radius as input.

r = float(input("Enter the radius: "))
pi = 3.14

area = pi*r*r
print(area)

#7️⃣ Take an integer input and print True if it is divisible by both 3 and 5, else False.

x = int(input("Enter the number: "))
if (x % 3 == 0) and (x % 5 == 0):
    print("True")
else :
    print("False")

#8️⃣ Assign 5 to variable a, 10 to b, and swap them without using a third variable.

a = 5
b = 10

a = a + b
b = a - b
a = a - b

print(a, b)


#9️⃣ Take two integers as input and print which one is larger.

x = int(input("Enter the first number: x: "))
y = int(input("Enter the second number: y: "))

if x>y:
    print(x, "is greater than ",  y)
else:
    print(y, "is greater than ", x)

#🔟 Given x = 7, y = 3, evaluate and print:
#x + y
#x - y
#x * y
#x / y
#x // y
#x % y
#x ** y

x = 7
y = 3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)