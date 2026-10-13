# // Exercise 6: Sum of N Natural Numbers
# //
# // Write a script that accepts a positive integer N from the user
# // and calculates the sum of all natural numbers from 1 to N.
# //
# // Formula:
# // Sum = N * (N + 1) / 2
# //
# // Sample Input:
# // N = 10
# //
# // Sample Output:
# // Sum: 55

n=int(input("Enter a positive number: "))
if n<1:
    print("Invalid input")
else:
    sum=n * (n + 1) // 2
    print(sum) 