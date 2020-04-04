inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

#inventory is a list of items that are in the warehouse for Bob’s Furniture. How many items are in the warehouse?
inventory_len = len(inventory)

#Select the first element in inventory. Save it to the variable first
first = inventory[0]

#Select the last item from inventory and save it to the variable last.
last = inventory[-1]

#Select items from the inventory starting at index 2 and up to, but not including, index 6.
inventory_2_6 = inventory[2:6]

#Select the first 3 items of inventory and save it to the variable first_3
first_3 = inventory[0:3]

#How many 'twin bed's are in inventory? Save your answer to twin_beds.
twin_beds = inventory.count('twin bed')

#ort inventory using .sort().
inventory.sort()
