# Exercise 11: Group Anagrams
# Write a program that starts with a list of strings defined at the top of your script 
# (e.g., words = ["eat", "tea", "tan", "ate", "nat", "bat"]) and groups the anagrams (words formed by rearranging letters) 
# together. Print the final grouped list of lists.

# Hardcoded Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


lst=["eat", "tea", "tan", "ate", "nat", "bat"]
temp=[]
sorted_word=["".join(sorted(i))for i in lst]
print(sorted_word)
if sorted_word not in temp:
    sorted_word
    print()
        
        
    
    
    
