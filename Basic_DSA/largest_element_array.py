#Find Largest Element in Array
#Method 1 — Using max()
arr = [10, 45, 23, 67, 89, 34]
largest = max(arr)
print("Largest element:", largest)

#Time Complexity: O(n)
#Space Complexity: O(1)

#Method 2 — Using Loop
arr = [10, 45, 23, 67, 89, 34]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)

#Time Complexity: O(n)
#Space Complexity: O(1)

#Method 3 — Using Sorting
arr = [10, 45, 23, 67, 89, 34]
arr.sort()
print("Largest element:", arr[-1])

#Time Complexity: O(n log n)
#Space Complexity: O(1)