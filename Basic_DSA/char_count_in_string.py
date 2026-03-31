"""
Input: apple
Output:
a : 1
p : 2
l : 1
e : 1
"""

#Method 1 — Using Dictionary
s = input("Enter string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
#Time Complexity: O(n)
#Space Complexity: O(n)
