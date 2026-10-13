products = [ 
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10}, 
    {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 20000, "quantity": 25} ,
    {"id": 4, "name": "Smartphone", "category": "Electronics", "price": 17800, "quantity": 12} ,
    {"id": 5, "name": "Smartphone", "category": "Electronics", "price": 31000, "quantity": 3} ,
    {"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50} ,
    {"id": 6, "name": "Smartphone", "category": "Electronics", "price": 200000, "quantity": 2} ,
] 

id_counter = len(products)

def menu():
    menu_text = '''1. Add product
    2. View all product
    3. Search product
    4. Update product
    5. Delete product
    6. Exit
    '''
    
    print("*****PRODUCT INVENTORY SYSTEM******")
    print(menu_text)
    try:
        choice = int(input("enter your choice: "))
    except:
        choice = -1
        
    return choice

def add_product():
    global id_counter
    
    name = input("enter your name: ")
    if name == "":
        print("name should not be empty!!")
        return
        
    category = input("enter category: ")
    if category =="":
        print("category should not be empty!!")
        return
    price = int(input("enter the price of the product: "))
    if price <=0:
        print("price should be greater then 0")
        return
    quantity = int(input("enter quantity of the product: "))
    if quantity<0:
        print("quantity should not be less then 0")
        return
    
    products.append(dict(id=id_counter+1, name=name, category=category, price=price, quantity=quantity))
    id_counter+=1
    
def search_product():
    
    print("1. search by id: ")
    print("2. search by name: ")
    
    choice = int(input("enter your choice: "))
    
    if choice ==1:
        
        id = int(input("enter id you want to search: "))
        
def main():
    while True:
        choice = menu()
        
        match choice:
            case 1:
                add_product()
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 5:
                ...
            case 6:
                ...
            case 7:
                ...
            
if __name__ == '__main__':
    main()