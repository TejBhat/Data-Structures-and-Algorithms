#Compute:
#x^n
#Example:
#2^3 = 8

#Method 2 — Using Loop
x = int(input("Enter base: "))
n = int(input("Enter power: "))

result = 1
for i in range(n):
    result *= x

print("Result:", result)

## Complexity: O(n)
#Space Complexity: O(1)

#Method 3 — Using Recursion
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

x = int(input("Enter base: "))
n = int(input("Enter power: "))

print("Result:", power(x, n))

#Time Complexity: O(n)
#Space Complexity: O(n) (recursion stack)