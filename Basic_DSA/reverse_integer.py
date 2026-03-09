#Input: 1234
#Output: 4321
#Method 1 — Using Math
def reverseNumber(n):
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
        
    return rev

print(reverseNumber(1234))

#Time Complexity: O(d)
#Space Complexity: O(1)

#Method 2 — Using String
def reverseNumber(n):
    return int(str(n)[::-1])

print(reverseNumber(1234))

#Time Complexity: O(d)