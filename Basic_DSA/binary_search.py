#Repeatedly divide the array into half.

#Example
#Array = [10, 20, 30, 40, 50]
#Target = 30
"""
Step 1
Middle = 30
Found ✅

Another example:

Target = 40

Step 1

Middle = 30
40 > 30 → search right

Step 2

Middle = 40
Found ✅
"""
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


arr = [10, 20, 30, 40, 50]

print(binary_search(arr, 40))

#Time Complexity	O(log n)
#Space Complexity	O(1)
#Because every step cuts the array in half.

#Why Binary Search needs sorted array?
#Binary search relies on comparison direction.
#Because the algorithm decides whether to search left or right based on the order of elements, which is only valid in a sorted array.
"""
What does log n mean?
log₂(n) means:
How many times we can divide n by 2 until we reach 1
Binary search works by dividing the array into half repeatedly.

Why O(log n)?
Because binary search halves the search space every step, so the number of steps equals log₂(n).
"""