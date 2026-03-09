#Find Third Largest Element
#Method 1 — Using Sorting
arr = [10, 45, 23, 67, 89, 34]
arr.sort()
print("Third largest:", arr[-3])

#Time Complexity: O(n log n)

#Method 2 — Using Loop (Efficient)
arr = [10, 45, 23, 67, 89, 34]
first = second = third = float('-inf')
for num in arr:
    
    if num > first:
        third = second
        second = first
        first = num
        
    elif num > second and num != first:
        third = second
        second = num
        
    elif num > third and num != second and num != first:
        third = num

print("Third largest:", third)

#Time Complexity: O(n)
#Space Complexity: O(1) ✅ Best