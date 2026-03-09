#Input:  "madam"
#Output: Palindrome

#Input:  "hello"
#Output: Not Palindrome

#Method 1 — Using String Slicing
s=input("Enter a string: ")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")    
#Time Complexity: O(n)
#Space Complexity: O(n)

#Method 3 — Using Two Pointers
s = input("Enter a string: ")
left=0
right=len(s)-1
flag=True

while left<right:
    if s[left]!=s[right]:
        flag=False
        break
    left+=1
    right-=1
if flag:
    print("Palindrome")
else:
    print("Not Palindrome")   

#Time Complexity: O(n)
#Space Complexity: O(1)     