# Exercise 8: Name Anonymizer
# Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. The output should print the initials of the first and middle names followed by the full last name. If the name consists of only a single word, print it as-is.

# Sample Input: "Vinod Kumar Kayartaya"
# Sample Output: "V. K. Kayartaya"
# Sample Input: "Bangalore"
# Sample Output: "Bangalore"

name=input("Enter your full name: ")
data=name.split()

if len(data) == 1:
    print(name)
elif len(data) == 2:
    print(data[0][0]+".", data[1])
else:
    print(data[0][0]+".", data[1][0]+".",data[2])
    
        
        