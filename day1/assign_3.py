# Exercise 3: Prime Number Checker
# Write a program that checks whether a positive integer entered by the user is a prime number.

# Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
# Sample Input: 17
# Sample Output: 17 is a prime number.

num=int(input("Enter a positve number: "))
if num<2:
    print("Invalid input")
else:    
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")
