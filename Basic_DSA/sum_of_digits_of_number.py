#Sum of Digits of a Number

#Input: 1234
#Output: 10
#Explanation: 1 + 2 + 3 + 4

#Method 1 — Using While Loop
def sumDigits(n):
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
        
    return total

print(sumDigits(1234))

#Time Complexity: O(d)
#(d = number of digits)
#Space Complexity: O(1)

#Method 2 — Using String
def sumDigits(n):
    return sum(int(d) for d in str(n))

print(sumDigits(1234))

#Time Complexity: O(d)