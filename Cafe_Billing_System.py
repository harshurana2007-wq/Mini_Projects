# Cafe Billing System

menu = {
    1: ("Coffee", 50),
    2: ("Tea", 30),
    3: ("Burger", 100),
    4: ("Pizza", 150),
    5: ("Sandwich", 80),
    6: ("Cold Drink", 40),
    7: ("Cake", 70)
}

total = 0
bill = []

print("=" * 40)
print("       ☕ WELCOME TO OUR CAFE")
print("         CAFE BILLING SYSTEM")
print("=" * 40)

while True:
    print("\n----------- MENU -----------")

    for number, item in menu.items():
        print(f"{number}. {item[0]:15} ₹{item[1]}")

    print("0. Generate Bill")

    choice = int(input("\nEnter item number: "))

    if choice == 0:
        break

    if choice in menu:
        quantity = int(input("Enter quantity: "))

        item_name = menu[choice][0]
        price = menu[choice][1]
        amount = price * quantity

        bill.append((item_name, price, quantity, amount))
        total += amount

        print(f"{item_name} x {quantity} added.")
        print(f"Amount: ₹{amount}")

    else:
        print("Invalid choice!")

# Generate Bill
print("\n")
print("=" * 50)
print("                 CAFE BILL")
print("=" * 50)

print(f"{'Item':15} {'Price':>8} {'Qty':>5} {'Amount':>10}")
print("-" * 50)

for item, price, quantity, amount in bill:
    print(f"{item:15} ₹{price:7} {quantity:5} ₹{amount:9}")

print("-" * 50)

gst = total * 0.05
grand_total = total + gst

print(f"{'Subtotal':30} ₹{total:.2f}")
print(f"{'GST (5%)':30} ₹{gst:.2f}")
print(f"{'Grand Total':30} ₹{grand_total:.2f}")

print("=" * 50)
print("       Thank You! Visit Again ☕")
print("=" * 50)