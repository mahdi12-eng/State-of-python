# Create a script that generates a new list containing only the names of items
#  that are out of stock (quantity is 0) and prints that list.
inventories = [
    {"item": "Laptop", "quantity": 5, "price": 1200},
    {"item": "Mouse", "quantity": 0, "price": 25},
    {"item": "Monitor", "quantity": 10, "price": 200},
    {"item": "Keyboard", "quantity": 0, "price": 50}
]

# list for zero values
script_list = []
print("Inventories:")
for inventory in inventories:
    print(inventory)
    for key,value in inventory.items():
        if isinstance(value,int) and value == 0:
            script_list.append(inventory['item'])

print()
print(f" The inventories which it's quantity  is 0:  {script_list}")