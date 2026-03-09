#Input: [1,2,4,5]
#Output: 3
#Formula:
#n(n+1)/2

#Method 1 — Using Sum Formula
arr = [1,2,4,5]
n = len(arr) + 1
expected = n*(n+1)//2
actual = sum(arr)
print("Missing:", expected - actual)
#Time Complexity: O(n)
#Space Complexity: O(1) ✅

#Method 2 — Using Set
arr = [1,2,4,5]

n = len(arr) + 1

s = set(arr)

for i in range(1, n+1):
    if i not in s:
        print(i)

#Time Complexity: O(n)
