#Find Second Largest Element
#Method 1 — Using Sorting
arr = [10, 45, 23, 67, 89, 34]
arr.sort()
print("Second largest:", arr[-2])

#Time Complexity: O(n log n)

#Method 2 — Using Loop (Better)
arr = [10, 45, 23, 67, 89, 34]
largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)

#Time Complexity: O(n)
#Space Complexity: O(1) ✅ Best