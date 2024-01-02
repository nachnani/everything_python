#inital list of products
products = ['phone', 'tablet', 'computer', 'laptop', 'journal']

#displaying initial list of products
print(f"Current list of items is:{products}")

#removing products
remove_item = input("Enter product to remove: ")
products.remove(remove_item)

#displaying list after product removal
print(f"Current list of items is:{products}")

#adding products
add_item = input("Enter product to add: ")
products.append(add_item)

#displaying list after adding products
print(f"Current list of items is:{products}")

#inital list of products
products = ['phone', 'tablet', 'computer', 'laptop', 'journal']

#displaying initial list of products
print(f"Current list of items is:{products}")

#adding products
add_item = input("Enter product to add: ")

# Accept product after where you want to place the current product
add_after = input(f"After which product do you want to place {add_item} ?")
index = products.index(add_after)
print(index)
products.insert(index + 1, add_item)

# displaying list after adding products
print(f"Current list of items is:{products}")