my_dict = {
    "name" : "Aninda",
    "age" : 21,
    "city" : "Kolkata"

}
print(my_dict)
print(my_dict.get("age"))

my_dict["branch"] = "CSE"
my_dict["is_passed"] = "True"

print(my_dict)


# LOOP in Dictionar
# FOR (key)
for key in my_dict:
    print(key)
# FOR (Value)
for value in my_dict:
    print(value)

# FOR (key, value)
for key,value in my_dict.items():
    print(key, "=>", value)


