"""

File Catlog Management System

"""


import json
import csv
books = []

i_counter = max([b['id'] for b in books], default=0)

def menu():
    options = '''
                1:Add Book
                2:View Catlog
                3:Search Books
                4:Update Details
                5:Delete Book
                6:Save To File
                7:Load from File
                8:Exit
    '''
    
    print(options)
    try:
        choice = int(input("Enter your Choice : ").strip())
        return choice
    except ValueError:
        return -1

def save_to_file():
    ''' JSON'''
    
    # try:
    #     with open('data.json', 'w') as file:
    #         json.dump(books,file, indent = 3)
    #         print("Data has been Saved in JSON ")
            
    # except Exception as e:
    #     print(f"Data was not saved in the File for some reasoins {e} ")   
    
    
    '''CSV'''   
    try:
        with open('data.csv', 'w', newline='') as file:
            writer = csv.DictWriter(
                file,
                fieldnames=['id', 'name', 'author', 'price']
            )
            
            writer.writeheader()
            writer.writerows(books)
            
        print("Data has been saved to CSV successfully.")

    except Exception as e:
        print(f"Data was not saved: {e}")

        
        
def load_from_file():
    try:
        with open('data.json', 'r') as file:
            books.extend(json.load(file))
            print("Data has been Loaded Successfully... ")
            
    except Exception as e:
        print(f"Data was not saved in the File for some reasoins {e} ") 
        
        
def add_book():
    global i_counter
    print("-" * 50)
    print("*****  Book Details  *****")
    print("-" * 50)
    
    name = input(" Enter the Name of the Book : ").strip()
    if name == "":
        print("Name cannot be Empty")
        return
            
    author = input("Enter the Name of the Author : ").strip()
    if author == "":
        print("Author cannot be Empty !!")
        return
    
    try:
        price = int(input(" Enter the Price : ").strip())
        
    except ValueError:
        print("Price should be Numeric")
        return
    
    if price <= 0:
        print("Price should always be > 0")
        return
    
    i_counter += 1
    
    books.append(dict(id = i_counter , name = name, author = author, price = price))
    print("Book has been Added Successfully ")   
    
def view_one_book(b):
    
    b_id, name, author, price = books[0].values()
    
    print("-" * 30)
    print("*****  Book Details  *****")
    print(f"ID:         {b_id}  ")
    print(f"Name:       {name} ")
    print(f"Author:     {author}  ")
    print(f"Price:      {price}  ")
    
    print("-" * 30)
    
    
def view_many_books(books):
    
    print('*' * 60)
    print("********  Book Management System  *******")
    print('*' * 60)
    
    print(f"{'ID':^8}{'Name':<15}{'Author':<10}{'Price':>10}")
    
    for b in books:
        print(f"{b['id']:^8}{b['name']:<15}{b['author']:<10}{b['price']:>10}")
        
        
    print('*' * 60)    
    
        
         
                          
def view_books():
    
    if len(books) == 0:
        print("No Books in the Sytem")
        return
    elif len(books) == 1:
        view_one_book(books[0])
    else:
        view_many_books(books)                    
    
def main():
    while True:
        choice = menu()
        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            ...
        elif choice == 4:
            ...
        elif choice == 5:
            ...          
        elif choice == 6:
            save_to_file()
        elif choice == 7:
            load_from_file()
        elif choice == 8:
            break
        else:
            print("Invalid Choice")  
            
            
if __name__ == '__main__':
    main()                      