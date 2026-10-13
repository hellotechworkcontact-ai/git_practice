filename = input("enter file name: ")

try:
    with open(filename,'r') as f1:
    
        print("here is the content of the file: ")
        print('-'*50)
        print(f1.read())
                                                         
except FileNotFoundError:
    print(f"There is no such file- {filename}")
    