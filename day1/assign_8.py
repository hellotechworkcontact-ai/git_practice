# Exercise 8: Score to Grade Converter
# Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

num=int(input("Enter a number: "))
if num>=90 and num<=100:
    print("Your grade: A ")
elif num>=80 and num<=89:
    print("Your grade: B ")
elif num>=70 and num<=79:
    print("Your grade: C ")
elif num>=60 and num<=69:
    print("Your grade: D ")
elif num>=0 and num<60:
    print("Your grade: F")
else:
    print("Invalid input")