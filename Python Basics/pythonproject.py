menu = {
    "pizza" : 120,
    "coffe" : 80,
    "tea" : 30,
    "salad" : 50
}
print("welcome to priya resturant")
print("pizza : RS 120\ncoffe : 80 \ntea : 30 \n salad : 50")
order_total = 0
item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available")
another_order = input("do you want to add another item ?(yes\no) ")
if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"item{item_2}has been added to order")
    else:
        print(f"item{item_2}is not available!")
print(f"the total amount of item is {order_total}")

