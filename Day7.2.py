#✅ 10 Practice Questions
#1️⃣ What is the time complexity of accessing the 5th element in a list?
#Answer: O(1)

#2️⃣ What is the time complexity of this function?
def func(arr):
    for i in arr:
        print(i)
#Answer: O(n)



#3️⃣ What is the time complexity?
def func(arr):
    for i in arr:
        for j in arr:
            print(i, j)
#Answer: O(n^2)


#4️⃣ Determine time complexity
def func(arr):
    for i in arr:
        for j in range(10):
            print(i, j)
#Answer: O(n)




#5️⃣ Write a function that has O(log n) time complexity.
#Binary Search

#6️⃣ Write a function that sums the numbers 1 to n. What is its time complexity?
def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_(0))
#Answer: O(N)


#7️⃣ What is the time complexity of creating a list of size n?
def create_list(n):
    list = []
    for i in range (n):
        list.append(i)
    return list
print(create_list(5))
#Answer: 0(N)
    
    
    
#8️⃣ Explain why binary search is O(log n).
#Binary Search is O(log n) because it divides the problem into half each iteration. 
#This means that the number of iterations required to find an element grows logarithmically with the size of the input.





#9️⃣ What is the time and space complexity of this function?
def make_list(n):
    return [i for i in range(n)]
#Answer: time complexity: O(n), space complexity: O(n)


#🔟 Write a function that prints all pairs of elements in two lists of length n and m. What is the time complexity?
def print_pairs(list1, list2):
    
    for elem1 in list1:
        for elem2 in list2:
            print(elem1, elem2)

# Example usage:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print_pairs(list1, list2)
#Answer: 0(N)