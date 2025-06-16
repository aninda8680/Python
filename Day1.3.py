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