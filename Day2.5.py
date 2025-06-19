# 1) Function to check even or odd:

def is_even(n):
    return n % 2 == 0
print(is_even(10))

print("\n")

# 2) List of squares:
square = []
for i in range(1, 4):
    square.append( i * i)
    print(square)

print("\n")

# 3) Write a function to return the factorial of a number:
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
print(factorial(5))

print("\n")

# 4) Write a function to check if a  number is prime.
def prime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
print(prime(1))

print("\n")

# 5) write a function to reverse a string
def reverse_string(s):
    string = ""
    for i in s:
        string = i + string
    return string
print(reverse_string("Hello"))

print("\n")


# 6) create a list and remove all even numbers from it:
my_list = [1, 2, 3, 4, 5]
new_list = []
for num in my_list:
    if num %2 != 0:
        new_list.append(num)
print(new_list)

print("\n")


# 7) Count how many times an elemwnt appears in a list:
#my_list = [1, 2, 3, 2, 4, 5, 4]
#num = int(input("Enter the number:"))
#print(my_list.count(num))

print("\n")


# 8) Create a tuple and access elements
my_tuple = ("apple", 32, "banana", 2)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])

print("\n")


# 9)Convert a list to a tuple.

my_list = ["apple", "banana", "cherry"]
my_tuple = tuple(my_list)
print(my_tuple)

print("\n")


# 10) Create a dictionary of 5 students with roll number as key and name as value.

students = {
    1 : "Aninda",
    2 : "B",
    3 : "C",
    4 : "D", 
    5 : "E"
}

print(students)

print("\n")


# 11) Add a new student and print all students.

students["6"] = "F"
print(students)

print("\n")


# 12) Print names of all students whose roll number is even.

for roll, name in students.items():
    if int(roll) % 2 == 0:
        print(name)