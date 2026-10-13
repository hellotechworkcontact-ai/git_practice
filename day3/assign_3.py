# Exercise 3: The Cargo Train Scanner

# Scenario:
# A train has wagons carrying different resources:
# ["coal", "iron", "gold", "coal", "timber", "coal"]

# The train conductor wants to inspect the cargo.

# Write a program that prompts the user to enter a resource type (e.g., "coal" or "gold").

# Print the total number of wagons carrying that resource (using .count()).

# If the resource is on the train, print the index of the very first wagon carrying it (using .index()).

# If it is not found, print "Resource not found on train!".

# Sample Input:
# "coal"
# Sample Output:
# Number of coal wagons: 3
# First coal wagon is at index: 0

# Sample Input:
# "oil"
# Sample Output:
# "Resource not found on train!"



resource = ["coal", "iron", "gold", "coal", "timber", "coal"]
find = input("enter item name: ")

if find in resource:
    total_item=resource.count(find)
    print("total item:",total_item)
    first_wagon=resource.index(find)
    print("first wagon index:",first_wagon)
else:
    print("resourse not found ")