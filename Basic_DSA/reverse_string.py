#Problems  
#1.Reverse words only "python at good very am I"
#2.Reverse letters only "I ma yrev doog ta nohtyp" 
#3.Reverse words + letters "nohtyp ta doog yrev ma I"

#problem-1
#Input: s = "I am very good at python"
#output:python at good very am I

#Method 1 — Using split() and reverse()

s="I am very good at python"
words=s.split()
words.reverse()
result=" ".join(words)
print(result)

#Time Complexity: O(n)
#Space Complexity: O(n)


#Method 2 — Using slicing
s="I am very good at python"
result="".join(s.split()[::-1])
print(result)

#Time Complexity: O(n)
#Space Complexity: O(n)


#problem-2
#Input: s = "I am very good at python"
#output:I ma yrev doog ta nohtyp

#Method 1 — Reverse each word
s="I am very good at python"
words=s.split()
result=[]
for w in words:
    result.append(w[::-1])
print(" ".join(result))
#Time Complexity: O(n)
#Space Complexity: O(n)

#Method 2 — Using list comprehension
s = "I am very good at python"
result=" ".join([word[::-1] for word in s.split()])
print(result)
#Time Complexity: O(n)
#Space Complexity: O(n)


#problem-3
#Input: s = "I am very good at python"
#output: nohtyp ta doog yrev ma I

#Method 1 — Reverse whole string
s = "I am very good at python"
print(s[::-1])
#Time Complexity: O(n)
#Space Complexity: O(n)

#Method 2 — Reverse words then letters
s = "I am very good at python"
words=s.split()[::-1]
result=[]
for w in words:
    result.append(w[::-1])

print(" ".join(result))


