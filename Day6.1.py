text = "data"
for c in text:
    print(c)




print("Hello\nWorld")
print("He said: \'Python is awesome!\'")


#Reverse a string

s = "python"
reverse = s[::-1]
print(reverse)
print("")

#Count Vowels

s = "hello world"
count = 0
for c in s:
    if c in "aeiou":
        count += 1
print("Vowles: ", count)
print("")

#Check Palindrome

s = "world"

if s == s[::-1]:
    print(s, "is palindrome")
else:
    print(s, "is not palindrome")
print("")


#✅ 10 Practice Questions

#1️⃣ Write a program to input a string and print its length.

s = "Hiii, I am Aninda."
print(len(s))
print("")

#2️⃣ Print the first and last character of a string.

print(s[0])
print(s[-1])
print("")
#3️⃣ Convert a string to uppercase and lowercase.

print(s.lower())
print(s.upper())
print("")

#4️⃣ Check if a string starts with "Hello".

print("Hiii" in s)
print("")

#5️⃣ Replace all spaces in a string with hyphens.

replace = s.replace(" ", "-")
print(replace)
print("")

#6️⃣ Count how many times 'a' occurs in "banana".
str = "banana"
count = str.count("a")
print(count)
print("")

#7️⃣ Input a string and print it in reverse.

str = "apple"
reverse = str[::-1]
print(reverse)
print("")

#8️⃣ Split a sentence into words and print the list.

str = "I am Aninda."
split = str.split()
print(split)
print("")

#9️⃣ Check if a string is a palindrome.

str = "madam"
if str == str[::-1]:
    print(str, "is palindrome")
else:
    print(str, "is not palindrome")

#🔟 Write a program that inputs a sentence and counts the number of vowels.

str = input("Enter a String:")
for c in str:
    if c in "aeiou":
        count += 1
print("Vowels: ", count)