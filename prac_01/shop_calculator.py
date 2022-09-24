items = int(input("Number of items: "))
total = 0
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
else:
    for i in range(0, items):
        item_price = float(input("Price of item: "))
        total += item_price
if total > 100:
    total -= (total * .1)
print(f"Total price for {items} items is ${total:.2f}")