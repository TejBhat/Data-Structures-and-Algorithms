#Method 1 — Using Loop
num = int(input("Enter number: "))

fact = 1

for i in range(1, num+1):
    fact = fact * i

print("Factorial:", fact)
#Time Complexity: O(n)
#Space Complexity: O(1)

#Method 2 — Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter number: "))

print("Factorial:", factorial(num))
#Time Complexity: O(n)
#Space Complexity: O(n) (recursion stack)