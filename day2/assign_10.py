# # Exercise 10: Run-Length String Compression
# # Write a program that prompts the user to enter a text string and compresses it using run-length encoding
# # (listing character counts next to each repeated character).
# # If the compressed string is not smaller in size than the original string, print the original string.

# # Sample Input: "aabcccccaaa"
# # Sample Output: "a2b1c5a3"
# # Sample Input: "abcd"
# # Sample Output: "abcd" (since "a1b1c1d1" is longer than "abcd")

def data():
    text=input("Enter the text: ")
    counter=1
    dump=[]
    for i in range(0,len(text)-1):    
        if text[i]==text[i+1]:
            counter+=1
        else:
            dump.append(f"{text[i]}{counter}")
            counter=1
    dump.append(f"{text[-1]}{counter}")        
    if len(dump)<len(text):
        print(f"{"".join(dump)}")
    else:
        print(text)
     
data()
            

    
