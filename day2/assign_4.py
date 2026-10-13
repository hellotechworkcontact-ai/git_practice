# ### Exercise 4: Vowel & Consonant Frequency

# Write a program that prompts the user to enter a string and counts:

# 1. The individual frequency of each vowel (`a`, `e`, `i`, `o`, `u`), case-insensitively.
# 2. The total count of all consonants.

# - **Sample Input**: `"Vinod Kumar Kayartaya"`
# - **Sample Output**:
#   ```text
#   Vowel Frequencies:
#   a: 4
#   e: 0
#   i: 1
#   o: 1
#   u: 1
#   Total Consonants: 12

text = input("enter text: ")

vowels = "aeiou"

for i in vowels:
    count = text.lower().count(i)
    print(i + ":",count)

cons_count=0
for i in text:
    if i in vowels:
        continue
    else:
        cons_count+=1

        
print(cons_count)