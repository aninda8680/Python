# Print the reverse triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Print pyramid
for i in range(1, 4):
    print(" " * (5-i), end="")
    print("*" * (2 * i - 1))

