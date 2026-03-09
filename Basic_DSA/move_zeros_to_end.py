#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]

#Method 1 — Using Loop
arr = [0,1,0,3,12]
result = []
for num in arr:
    if num != 0:
        result.append(num)
zeros = arr.count(0)
result.extend([0]*zeros)
print(result)

#Time Complexity: O(n)
#Space Complexity: O(n)

#Method 2 — In-place Method (Best)
arr = [0,1,0,3,12]
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print(arr)

#Time Complexity: O(n)
#Space Complexity: O(1) ✅