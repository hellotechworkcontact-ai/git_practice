# Exercise 2: Fibonacci Sequence Generator
# Write a Python script to print the first 
# N
#  terms of the Fibonacci sequence, where 
# N
#  is provided by the user.

# Fibonacci sequence: 

# Sample Input: N = 6
# Sample Output: 0, 1, 1, 2, 3, 5

n=int(input("Enter the value of N: "))
a=0
b=1
for i in range(n):
    print(a,end=","if i<n-1 else"")
    a,b=b,a+b