#Two strings are anagrams if they contain same characters in different order.
#listen
#silent

#Method 1 — Using Sorting
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#Time Complexity: O(n log n)

#Method 2 — Using Character Count
from collections import Counter
s1 = "listen"
s2 = "silent"

if Counter(s1) == Counter(s2):
    print("Anagram")
else:
    print("Not Anagram")

#Time Complexity: O(n) ✅