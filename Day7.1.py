
#Linear Time Complexity O(n)
def print_all(arr):
    for i in arr:
        print(i)

arr = [1, 3, 5, 7, 9]
print_all(arr)

# Quadratic Time Complexity O(n^2)
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
arr = [1, 2, 3]
print_pairs(arr)

# Space COMPLEXITY

def create_array(n):
    arr = []
    for i in range(n+1):
        arr.append(i)
    return arr
n=5


result = create_array(n)
print(result)


#