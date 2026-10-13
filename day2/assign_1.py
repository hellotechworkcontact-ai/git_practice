''''Write a Python program that prompts the user to enter a sentence. The program must count and display:

1. The total number of characters (including spaces and punctuation).
2. The total number of words.
- **Sample Input**: `"Learning Python is fun!"`
- **Sample Output**:
  ```text
  Total Characters: 23
  Total Words: 4
  ```
  '''



sen=input("Enter the sentence:")
total_char=len(sen)
total_word=len(sen.split())
print("Total character: ",total_char)
print("Total number of words: ",total_word)