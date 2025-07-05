coordinates = (10, 20)
coordinates[0]
coordinates[1]

print(coordinates[0])

a, b = (1, 2)
print(a, b)


#Dictioinary

student = {
    "name": "Alice", 
    "age": 20,
    "marks": 85
}

#updating
student["age"] = 24

#adding
student["grade"] = "B"

#deleting
del student["marks"]



print(student)
print(student.keys())
print(student.values())
print(student.items())

print("")
#Check if any key exist
if "grade" in student:
    print("Grade Exists")
else: 
    print("hHey")

print("")
#Looping over Dictionary
for key, value in student.items():
    print(key, ":", value)

print("")
#1️⃣ Create a tuple containing the numbers 1 to 5 and print it.

tuple = (1, 2, 3, 4, 5)
print(tuple)

#2️⃣ Access the third element of the tuple (10,20,30,40,50) and print it.
print("")
tuple = (10, 20, 30, 40, 50)
third_element = tuple[2]
print(third_element)

print("")
#3️⃣ Create a set from the list [1,2,2,3,4,4,5] and print it.

list = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list)
print(set_from_list)

print("")
#4️⃣ Add element 6 to the set {1,2,3}.

set = {1, 2, 3}
set.add(6)
print(set)

print("")
#5️⃣ Find the intersection of sets {1,2,3} and {2,3,4}.

a = {1, 2, 3}
b = {2, 3, 4}
intersection = a & b
print(intersection)

print("")
#6️⃣ Create a dictionary with keys name, age, and city. Fill them with your data and print the dictionary.

my_dict = {
    "name" : "Aninda",
    "age" : 21,
    "city" : "Kolkata",
    
}

print(my_dict)

print("")
#7️⃣ Update the age in the dictionary to a new value.

my_dict["age"] = 22
print(my_dict)

print("")
#8️⃣ Delete the city key from the dictionary.

del my_dict["city"]
print(my_dict)

print("")
#9️⃣ Check whether the key name exists in your dictionary.

if "name" in my_dict:
    print("Exists")

print("")
#🔟 Loop over your dictionary and print all key-value pairs.

for keys, values in my_dict.items():
    print(keys, "->", values)