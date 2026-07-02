cart = []
prices = {}

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Total Bill")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.append(item)
        prices[item] = price

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            prices.pop(item)

    elif choice == 3:
        print("Cart:", cart)

    elif choice == 4:
        total = sum(prices.values())
        unique_items = set(cart)

        print("Total Bill:", total)
        print("Unique Categories:", unique_items)

    elif choice == 5:
        break
