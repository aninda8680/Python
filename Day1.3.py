# 1) Find largest numnber of two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
        
if a > b :
        print(a, " is the largest number. ")
elif a < b:
        print(b, "is the largest number. ")
else: 
        print("Both number are equal. ")



# 2) Check if number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
        print(num, "is an even number. ")
else:
        print(num, "is an odd number. ")


# 3) Take 2 numbers from user and print their sum and product

num2 = int(input("Enter the first number: "))
num3 = int(input("Enter the second number: "))
sum = num2 + num3
product = num2 * num3
print("The sum of", num2, "and", num3, "is:", sum)
print("The product of", num2, "and", num3, "is", product)


# 4) Check whether a given number is divisible by 5

num1 = int(input("Enter a number: "))
if num1 % 5 == 0:
        print(num1, "is divisible by 5.")
else:
        print(num1, "is not divisible by 5 ")


# 4) Take a number and print whether it's positive, negative or zero.

num = int(input("Enter a number: "))
if num > 0:
        print(num, "is a positive number.")
elif num < 0:
        print(num, "is a negative number.")
else:
        print("The number is zero.")
        


# 5) Check if a number is in the range 10 to 100.

num = int(input("Enter the number: "))
if num >= 10 and num <= 100:
        print (num, "is in the range of 10 and 100.")
else:
        print("The num is not in the range.")



# 6) Take 3 numbers and print the largest.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if num1 >= num2 and num1 >= num3:
        print(num1,"is the largest no." )
elif num2 >= num1 and num2 >= num3:
        print(num, "is the largest no.")
else:
        print(num3, "is the largest no.")




# 7) Write a program to check whether a year is a leap year.

year = int(input("Enter a year: "))
if ( year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 )):
        print(year, "is a leap year. ")
else:
        print(year, "is not a leap year. ")



# 8) Take a number from the user and:
#  If it's divisible by both 3 and 5 → print "FizzBuzz" 
# If only by 3 → print "Fizz" 
# If only by 5 → print "Buzz" Otherwise, 
# print the number itself

num = int(input("Enter the number: "))

if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
elif num % 3 == 0:
        print("Fizz")
elif num % 5 == 0:
        print("Buzz")
else:
        print(num)