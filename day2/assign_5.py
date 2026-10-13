# Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters). **Do not use Python's built-in `.title()` method.**

# - **Sample Input**: `"WELCOME TO BANGALORE CITY"`
# - **Sample Output**: `"Welcome To Bangalore City"`


text=input("Enter text: ")
words=text.split()
result=""
for i in words:
    i=i.lower()
    i=i[0].upper()+i[1:]
    result+=i+" "
print(result)