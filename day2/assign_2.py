'''
### Exercise 2: Reversed Uppercased String

Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

- **Sample Input**: `"Bangalore"`
- **Sample Output**: `"EROLAGNAB"` 
'''

city=input("Ënter the city name: ")
upper_city=city.upper()
print(upper_city)
rev=upper_city[::-1]
print(rev)


