def Burgerbuyer(burger_name, location="Mohakhali"):
    price = 0

    if burger_name == "BBQ Chicken Cheese Burger":
        price = 250
    elif burger_name == "Beef Burger":
        price = 170
    elif burger_name == "Naga Drums":
        price = 200

    tax = (8 / 100) * price

    if location == 'Mohakhali':
        delivery_charge = 40
    else:
        delivery_charge = 60

    total = price + tax + delivery_charge

    return total


print(Burgerbuyer("Beef Burger", "Dhanmondi"))
print(Burgerbuyer("Beef Burger"))
