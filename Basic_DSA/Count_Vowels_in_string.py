#Count Vowels in a String
#@Input: hello world
#Output: 3

#Method 1 — Using Loop
s = input("Enter string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels:", count)
#Time Complexity: O(n)
#Space Complexity: O(1)