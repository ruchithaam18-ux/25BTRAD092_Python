print("----- BILL GENERATOR -----")

n = int(input("Enter number of items: "))

subtotal = 0

for i in range(n):
    print(f"\nItem {i + 1}")
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    subtotal += price

gst = subtotal * 0.18
total = subtotal + gst

print("\n----- BILL -----")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Total Amount: ₹{total:.2f}")