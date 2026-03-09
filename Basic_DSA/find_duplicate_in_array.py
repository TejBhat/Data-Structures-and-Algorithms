#Input: [1,2,3,2,4,1]
#Output: 1 2

#Method 1 — Using Set

arr = [1,2,3,2,4,1]

seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
#Time Complexity: O(n)
#Space Complexity: O(n)

#Method 2 — Using Nested Loop
arr = [1,2,3,2,4,1]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[i])

#Time Complexity: O(n²) ❌
#Space Complexity: O(1)