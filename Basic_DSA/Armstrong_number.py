#An Armstrong number is a number where the sum of digits raised to the power of number of digits equals the number itself.
"""
153
1³ + 5³ + 3³ = 1 + 125 + 27 = 153
"""
#Method 1 — Using While Loop
num = int(input("Enter number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong")

#Time Complexity: O(d)
#(d = number of digits)
#Space Complexity: O(1)

#Method 2 — Works for Any Number of Digits
num = int(input("Enter number: "))

digits = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not Armstrong")
#Input: 153
#Output: Armstrong number

