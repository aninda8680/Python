# 🟢 Easy:

# 1. Traverse and print elements of an array in reverse.
# Example:
arr = [1, 2, 3, 4, 5]
# Output should be: 5 4 3 2 1
for i in arr[::-1]:
    print(arr[i], end=" ")


# 2. Insert a number at a given index from user input.
# Example: Insert 99 at index 2 → [1, 2, 99, 3, 4, 5]
arr = [1, 2, 3, 4 , 5]
arr.insert(2, 99)
print(arr)

# 3. Delete the first and last element of an array.
# Before: [1, 2, 3, 4, 5] → After: [2, 3, 4]
arr = [1, 2, 3, 4, 5]
del arr[0]
arr.pop()
print(arr)

# 4. Count how many times a value appears in the array.
# arr = [1, 2, 2, 3, 2, 4]
# Count of 2 => 3
arr = [1, 2, 3, 4, 2, 2]
c = arr.count(2)
print(c)



# 🟡 Medium:

# 5. Shift all elements to the right by 1.
# Input: [1, 2, 3, 4] → Output: [4, 1, 2, 3]
arr = [1, 2, 3, 4]
last = arr[-1]

final = [last] + arr[:-1]
print(final)


# q. Shift all elements to the right by 2.
# Input: [1, 2, 3, 4] → Output: [[3, 4, 1, 2]
arr = [1, 2, 3, 4]
k = 2
k = k % len(arr)
last = arr[-k:]
final = last + arr[:-k]
print(final)

# q. Shift all elements to the left by 1.
# Input: [1, 2, 3, 4] → Output: [2, 3, 4, 1]
arr = [1, 2, 3, 4]
first = arr[:-3]
final = arr[-3:] + first
print(final)

# 6. Remove duplicates from the array.
# Example: [1, 2, 2, 3, 3, 4] → [1, 2, 3, 4]
arr = [1, 2, 2, 3, 3, 4]
final = set(arr)
print(final)

arr = [1, 2, 2, 3, 3, 4]
def unique(arr):
    final = []
    for i in arr:
        if i not in final:
            final.append(i)
    return final

print(unique(arr))


# 7. Insert 2 elements at position 3 and print final array.
# Example: Insert [7, 8] at index 3 → [1, 2, 3, 7, 8, 4, 5]
arr = [1, 2, 3, 4, 5]
arr.insert(3, 7)
arr.insert(4, 8)
print(arr)

# 🔴 Hard:

# 8. Rotate array by k steps (right rotation).
# arr = [1, 2, 3, 4, 5], k = 2 → Output: [4, 5, 1, 2, 3]
arr = [1, 2, 3, 4, 5]
k = int(input("Enter the value of k: "))
k = k % len(arr)
last = arr[-k:]
first = arr[:-k]
final = last + first
print(final)

# 9. Merge two sorted arrays into one sorted array.
# a = [1, 3, 5], b = [2, 4, 6] → Output: [1, 2, 3, 4, 5, 6]
a = [1, 3, 5]
b = [2, 4, 6]

def merge(a, b):
    final = []
    while a or b:
        if not a:
            final += b
            break
        elif not b:
            final += a
            break
        elif a[0] < b[0]:
            final.append(a.pop(0))
        else:
            final.append(b.pop(0))
    return final
print(merge(a, b))


# 10. Find the second largest number in an array.
# Example: [1, 3, 4, 2] → Second largest: 3

arr = [1, 3, 4, 2]
a = max(arr)
arr.remove(a)
b = max(arr)
print(b)

arr = [1, 3, 4, 2, 2, 3]
arr = sorted(set(arr), reverse = True)
print(arr[1])

arr = [1, 3, 4, 2, 2, 3]
arr = sorted(set(arr))
print(arr[-2])

arr = [1, 3, 4, 2]
def second_largest(arr):
    arr = sorted(set(arr), reverse=True)
    if len(arr) < 2:
        return None
    return arr[1]
print(second_largest(arr))