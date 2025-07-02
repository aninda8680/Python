# sum of first N natural numbers
a = int(input("Enter N number: "))
total = 0
for i in range(1, a+1):
    total += i
print("Sum: ", total)

# FACTORIAL of a number
a = int(input("Enter the number: "))
fact = 1
for i in range (1, a+1):
    fact *= i
print("Fact: ", fact)

# while loop countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast Off!")



#1️⃣ Write a program to print numbers 1 to 10 using a for loop.

for i in range (1, 11):
    print(i)

#2️⃣ Write a program to print the multiplication table of a number entered by the user (up to 10).

n = int(input("Enter the number :"))
table = 1
for table in range (1, 11):
    print( n, " * ", table, " = ",  n*table)
    table += 1

#3️⃣ Check whether an input number is even or odd using if-else.

n = int(input("Enter the number :"))
if n % 2 ==0:
    print("Its EVEN")
else:
    print("ODD")

#4️⃣ Print all even numbers between 1 and 50.

for i in range(1, 51):
    if i % 2 == 0:
           print(i)


#5️⃣ Calculate the sum of all numbers from 1 to N using a while loop.

n = int(input("Enter the N number: "))
sum = 0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)


#6️⃣ Find factorial of a given number using a while loop.

n = int(input("Enter the number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(fact)

n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)



#7️⃣ Write a program that asks for a number and prints whether it is divisible by 3 and 5.

n = int(input("Enter the number: "))

if (n % 3 == 0) and (n % 5 == 0):
    print("Divisible by both")
elif n % 5 == 0:
    print("Divisible of 5")
elif n % 3 == 0:
    print("divisible by 3.")
else: 
    print("not divisible by any.")

#8️⃣ Print each character of a string input by the user on a separate line.

string = input("Enter the string: ")

for i in range(len(string)):
    print(string[i])

#9️⃣ Use break to stop printing numbers when you reach 7 in a loop from 1 to 10.

for i in range(1, 11):
    if i == 7:
        break
    print(i)

#🔟 Use continue to skip printing the number 5 in a loop from 1 to 10.

for i in range (1, 11):
    if i == 5:
        continue
    print(i)