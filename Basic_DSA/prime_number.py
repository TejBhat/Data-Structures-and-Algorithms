#A Prime Number is a number greater than 1 that has only two factors: 1 and itself.

num = int(input("Enter number: "))

count = 0

for i in range(1, num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not prime")

#Time Complexity: O(n)
#Space Complexity: O(1)

#Method 2 — Optimized Method

num = int(input("Enter number: "))

flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime number")
else:
    print("Not prime")

#Time Complexity: O(n)
#Space Complexity: O(1)