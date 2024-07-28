menu = {
    "Veg Fried Rice" : 170,
    "Egg Fried Rice" : 190,
    "Chicken Fried Rice" : 240,
    "Paneer Pulao" : 200,
    "Peas Pulao" : 200,
    "Chicken Dum Biryani" : 230,
    "Mutton Biryani" : 320
}
print("welcome to the Abhishek Prime Hotel and Restaurant")
print("veg fried rice :Rs 170\nEgg Fried Rice : 190\nChicken Fried Rice : 240\nPaneer Pulao : 200\n Peas Pulao : 200\n Chicken Dum Biryani : 230\nMutton Biryani : 320")
order_total = 0
item_1 = input("enter the name of the item you want to order =")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"your item{item_1} has been added to your order")
else:
    print(f"your order item{item_1} is not available!")
another_item = input("do you want to order another food?(yes\no) ")
if another_item == "yes":
    item_2 = input("enter the name of the item you want to order =")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"your item {item_2}has been added to your order") 
    else:
        print(f"your order item {item_2}is not available")    
print(f"the total amount of item is{order_total}")