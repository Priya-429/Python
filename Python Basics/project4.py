menu = {
    "Marghenta" : 279,
    "Tandoori Onion" : 359,
    "Veggie Tandoori" : 199,
    "Veggie Lover" : 269,
    "Double Paneer Supreme" : 529,
    "Chicken Tikka Supreme" : 629
}

print("welcome to Pizza Hut \n  Please come and take a seat ")
print("Marghenta : 279\n Tandoori Onion : 359\n Veggie Tandoori : 199\n Veggie Lover : 269 \n Double Paneer Supreme : 529 \n Chicken Tikka Supreme : 629")
order_total = 0
item_1 = input("enter the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"your item {item_1} is not available in our menu")
another_item = input("do you want to order another food (yes\no)")
if another_item == "yes":
    item_2 = input(f"your item has been added to your order ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item  {item_2}has been added to your order")
    else:
        print(f"your order item{item_2} is not available!")
print(f"Total amount you have to pay = ",order_total)
print("Thanks for ordering")

