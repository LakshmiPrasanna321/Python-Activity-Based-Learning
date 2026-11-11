n = int(input("Enter number of products: "))
grand_total = 0
for i in range(n):
    name = input("\nEnter product name: ")
    cat = input("Enter category (Electronics/Grocery/Clothing): ").lower()
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    sub = price * qty
    if cat == "electronics":
        tax = sub * 0.18
    elif cat == "grocery":
        tax = sub * 0.05
    else:
        tax = sub * 0.12
    total = sub + tax
    grand_total = grand_total + total
    print(f"{name}: Subtotal {sub}, Tax {tax}, Total {total}")
if grand_total > 5000:
    disc = grand_total * 0.10
elif grand_total > 2000:
    disc = grand_total * 0.05
else:
    disc = 0
if disc > 500:
    disc = 500
final = grand_total - disc
print("\n--- Invoice ---")
print("Grand Total:", grand_total)
print("Discount:", disc)
print("Final Payable:", final)
