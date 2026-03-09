#Input: [1,2,2,3,4,4]
#Output: [1,2,3,4]

#Method 1 — Using Set
arr = [1,2,2,3,4,4]
result = list(set(arr))
print(result)

#Time Complexity: O(n)
#Space Complexity: O(n)

#Method 2 — Using Loop
arr = [1,2,2,3,4,4]
result = []

for num in arr:
    if num not in result:
        result.append(num)

print(result)

#Time Complexity: O(n²) ❌