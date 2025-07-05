#EXAMPLES

#Tuple Unpacking
t = (10, 20, 30)
a, b, c = t
print(a)
print(b)
print(c)
print(t)

#Set Operations
a = {1, 2, 3}
b = {4, 5, 6}
union_set = a | b
print(union_set)


#Dictionary Iteration
data = {
    "name" : "Aninda", 
    "Age" : 25
}
for key, values in data.items():
    print(key + ":" + values)