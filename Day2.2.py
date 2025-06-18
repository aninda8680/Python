#LIST
# A lsi is a collection of items
# Alist is a mutable => Can change the items afer creating the lists  
#            ordered => it maintains the order in which there were added
#            indexed => Access items using index
#            collection of items. 
# It can hold heterogenous data-types --> different types of data-types 

my_list = [1, 3, 3, "Hello", "bye"]
print(my_list)

#Adds item(x) at the end of the list
my_list.append(5)
print(my_list)


# Insert item(x) at index i
my_list.insert(0,"Hi")
print(my_list)


#Removes and return item at index
my_list.pop()
print(my_list)


#Remove first occurence of x
my_list.remove("Hello")
print(my_list)


#Sorts the list in Ascending Order (should only comtain int/strings/numbers)
my_list.sort()
print(my_list)


#Reverses the list
my_list.reverse()
print(my_list)


#Returns a shallow copy of the list
my_list.copy()
print(my_list)


#Return idex of first(x)
print(my_list.index(1))


#Returns the count of x in the list
print(my_list.count(3))


# Empty the list
my_list.clear()
print(my_list)











