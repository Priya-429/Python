# Define the menu of restaurant
menu = {
    "Pizza" : 120,
    "Pasta" : 60,
    "Burger" : 110,
    "Salad" : 50,
    "coffee" : 50,
    "Tea"    : 30
}
print("welcome to Priya Restaurant")
print("Pizza : RS120\nPasta : RS60\nBurger : RS110\nSalad :RS 110\nCoeffe : RS50\nTea :RS 50")
order_total = 0
item_1 = input("enter the name of item you want to order =") 
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet")
another_order = input("do you want to add another item? (yes\no)")
if another_order == "yes":
    item_2 = input("enter the name of second item =  ")
    if item_2 in menu :
        order_total += menu[item_2]  
        print(f"item{item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")
print(f"the total amount of items is {order_total}")