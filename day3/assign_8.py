# Exercise 8: De-duplicating Shopping Cart
# Scenario: An online shopping cart has duplicate items due to double-clicks: ["apple", "banana", "apple", "orange", "banana", "banana"]. Write a program that processes the list and removes all duplicate items, but keeps the first occurrence of each item in its original order. Print the cleaned cart.

# Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
# Sample Output: ['apple', 'banana', 'orange']

carts = ["apple", "banana", "apple", "orange", "banana", "banana"]

new_cart = []
for item in carts:
    if item not in new_cart:
        new_cart.append(item)
print(new_cart)