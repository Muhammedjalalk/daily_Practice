inventory={
    "mouse":5,
    "keyboard":6,
    "monitor":20,
    "laptop":10,
    "printer":3
}

print("All Inventory:")
for product in inventory:
    print(product,":",inventory[product])


print("\n Greater then 10:")

for product in inventory:
    if inventory[product]>10:
        print(product,":",inventory[product])

print("\n Less then 10")
for product in inventory:
    if inventory[product]<10:
        print(product,":",inventory[product])


#update or add product
product="wire mouse"
quantity=15

if product in inventory:
    inventory[product]=quantity
    print("Quantity updated")
else:
    inventory[product]=quantity
    print("New Product added")

# 5.Display final inventory
for product in inventory:
    print(product,":",inventory[product])




