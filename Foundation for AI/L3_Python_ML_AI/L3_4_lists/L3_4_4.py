inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#1
inventory_len = len(inventory)
print(inventory_len)

#2
first = inventory[0]
print(first)

#3
last = inventory[-1]
print(last)

#4
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

#5
first_3 = inventory[:3]
print(first_3)

#6
twin_beds = inventory.count('twin bed')
print(twin_beds)

#7
removed_item = inventory.pop(4)
print(removed_item)

#8
inventory.insert(10,"19th Century Bed Frame")
print(inventory)

#9
inventory.sort()
print(inventory)
