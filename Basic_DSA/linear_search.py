#Check each element one by one until the target is found.

#Array = [10, 20, 30, 40, 50]
#Target = 30

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]

print(linear_search(arr, 30))
#Output
#2
#Complexity
#Time Complexity	O(n)
#Space Complexity	O(1)

#Worst case: check all elements.