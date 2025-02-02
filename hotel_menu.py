# DEFINE THE MENU OF RESTAURANT
menu = {
    "Pizza" : 105,
    "Pasta" : 50,
    "Burger" : 60,
    "Salad" : 70,
    "Coffee" : 80,
    "Maggiee" : 25,
}
print ("WELCOME TO MY PYTHON RESTAURANT")
print ("Pizza : Rs105\nPasta : Rs50\nBurger : Rs60\nSalad : Rs70\nCoffee : Rs80\nMaggiee : Rs25\n")

order_total = 0
# variable mein value store hoga  (80 + 0 = 80)
Item_1 = input ("Enter the name of the item you want to order = ")
if Item_1 in menu:
    order_total += menu [Item_1]
    print (f"Your item {Item_1}has been added to your order")

else :
    print ("Ordered item {Item_1} is not available yet!")

another_order = input ("Do you want to add another item? (Yes/No)? ")
if another_order == "Yes":
        Item_2 = input ("Enter the name of second item = ")
        if Item_2 in menu:
            order_total += menu [Item_2]
            print (f"Your item {Item_2} has been added to your order")
        else:
            print (f"Your item {Item_2} is not available yet!")

print (f"The total amount of the order is {order_total}")
