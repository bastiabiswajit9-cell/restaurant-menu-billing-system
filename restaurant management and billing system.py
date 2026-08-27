menu={
'Non veg role' :60,
'chicken pakoda' :70,
'Egg chop' :15,
'chicken lollypop':80,
'chicken biriyani':120,
'chicken chowmin':75,
'Egg chowmin':50,
'tandori chicken':210,
'chicken tandori fry':180,
'chicken tikka':190,
'chicken leg piece':130,
'veg role':60,
'mix veg role':70,
'paneer 65':185,
'veg biriyani':100,
'veg chowmin':60,
'Baby corn 65':170,
'paneer 555':210,
'sezwan paneer':220,
'veg manchurian':150
}
#greet
print("welcome to our restaurant")
print("veg menu")
print("veg role:  Rs60\nmix veg role: Rs70\npaneer 65:  Rs185\nveg biriyani:  Rs100\nveg chowmin:  Rs60\nBaby corn 65:  Rs170\npaneer 555:  Rs210\nsezwan paneer:  Rs220\nveg manchurian:  Rs150")
print("Non veg menu\nNon veg role: Rs60\nchicken pakoda:  Rs70\nEgg chop:  Rs15\nchicken lollypop:  Rs80\nchicken biriyani:  Rs120\nchicken chowmin:  Rs75\nEgg chowmin:  Rs50\ntandori chicken:  Rs210\nchicken tandori fry:  Rs180\nchicken tikka:  Rs190\nchicken leg piece:  Rs130")

order_total = 0
while True :
	item=input("Enter the name of the item do you want to order =")
	if item in menu:
		quantity = int(input("Enter the quantity of item="))
		item_total=menu[item]*quantity
		order_total += int(item_total)
		print(f"your ordered item is added on your order")
	else:
		print("ordered item is not available yet !")
	another_order=input("Do you want to order another_item ?(yes/No)")
	if another_order . lower()!="yes":
			break
	
print("___________")
print(f"Total amount to pay=Rs{order_total}")
print("___________")
print("thank you for visiting us")