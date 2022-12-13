quantity = int(input("enter the quantity: "))
cost = 100
price = quantity * cost
if quantity > 1000:
    discount = price * 0.1
    print("your total price with 10 percent discount ",discount)
else:
    print("your total price is ",price)
