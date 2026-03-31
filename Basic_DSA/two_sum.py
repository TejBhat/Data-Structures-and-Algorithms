#Problem:
#Given an array and a target, find two numbers whose sum equals the target.
#Input: arr = [2,7,11,15], target = 9
#Output: 2 + 7

#Method 1 — Using Dictionary (Best)
arr = [2,7,11,15]
target = 9

seen = {}

for num in arr:
    diff = target - num
    
    if diff in seen:
        print(diff, num)
        break
    
    seen[num] = True

#Time Complexity: O(n) ✅
#Space Complexity: O(n)

#Method 2 — Using Nested Loop
arr = [2,7,11,15]
target = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])

#Time Complexity: O(n²) ❌
#Space Complexity: O(1)