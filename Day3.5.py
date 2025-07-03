#1️⃣ **Write a function `greet_user` that takes a name and prints "Hello, <name>".**

def greet_user(name):
    print("Hello,", name)
greet_user("Ani")

#2️⃣ **Write a function that takes two numbers and returns their product.**

def product(a, b):
    return a*b
print(product(2, 3))

#3️⃣ **Write a function `is_even` that returns True if the number is even, False otherwise.**

def odd_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("odd")

n = int(input("Enter the number: "))
odd_even(n)

#4️⃣ **Write a recursive function to calculate the factorial of a number.**

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

n = int(input("Enter the number: "))
print(fact(n))

#5️⃣ **Write a function that takes a list and returns the sum of its elements.**

def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total
user_input = input("Enter the list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
result = sum_list(numbers)
print("Sum:", result)


#6️⃣ **Write a function with default argument `country="India"` that prints "<name> is from <country>".**

def country_name(name, country="India"):
    print(name, " is from ", country)
    
country_name("Aninda")


#7️⃣ **Write a lambda function that returns the square of a number.**

square = lambda x : x*x
x = int(input("Enter x: "))
print(square(x))


#8️⃣ **Write a function to find the maximum of three numbers.**

def max(a, b, c):
    if a > b and a > c:
        print(a, " is the largest")
    elif b > a and b > c:
        print(b, "is the largest")
    else:
        print(c, "is the largest")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
max(a, b, c)


#9️⃣ **Write a recursive function to compute the nth Fibonacci number.**

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
for i in range(7):
    print(fibonacci(i), end = " ")


#🔟 **Write a function that takes two numbers and returns both their sum and difference.**

def calc(a, b):
    return a+b, a-b
    

a = int(input("Enter a: "))
b = int(input("Enter b: "))

calc_sum, calc_diff = calc(a, b)
print(calc(a, b))   