
#1️⃣ **Create a list of integers from 1 to 10 and print it.**
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)


#2️⃣ **Print the last element of the list using negative indexing.**

print(list[-1])


#3️⃣ **Write a program to input 5 numbers from the user and store them in a list.**

num_list = []
for i in range(5):
    num = int(input("Entert the numbers: "))
    num_list.append(num)
print(num_list)


#4️⃣ **Given a list `[4,7,2,8,5]`, sort it in ascending order and print.**

num_list = [4, 7, 2, 8, 5]
num_list.sort()
print(num_list)

#5️⃣ **Remove the number 2 from the list `[1,2,3,2,4]`.**

num_list = [1, 2, 3, 4, 5]
num_list.remove(2)
print(num_list)

#6️⃣ **Using list comprehension, create a list of squares of numbers 1–10.**

squares = [x*x for x in range (1, 11)]
print(squares)

#7️⃣ **Reverse the list `[10,20,30,40,50]` and print.**

list = [10, 20, 30, 40, 50]
list.reverse()
print(list)

#8️⃣ **Count how many times 3 occurs in `[1,3,3,3,5,3]`.**

list = [1, 3, 3, 3, 5, 3]
num = list.count(3)
print(num)

#9️⃣ **Write a program that takes a list and prints all even numbers.**

list = []
for i in range(5):
    num = int(input("Enter the number: "))
    list.append(num)
print(list)

even = [x for x in list if x % 2 == 0]
print(even)

#🔟 **Given a 3×3 matrix list, print the element at row 2 column 3.**

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    
print(matrix [1][2])