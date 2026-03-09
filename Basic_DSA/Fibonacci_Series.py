#0 1 1 2 3 5 8 13 ...
#Formula: F(n) = F(n-1) + F(n-2)
#Method 1 — Using Loop
n = int(input("Enter number: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#Time Complexity: O(n)
#Space Complexity: O(1)

#Method 2 — Using Recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter number: "))

for i in range(n):
    print(fib(i), end=" ")
#Time Complexity: O(2^n) ❌ Slow
#Space Complexity: O(n)