budget = float(input("Enter budget in INR: "))
n = int(input("Enter number of expense categories: "))
total = 0
largest = ""
largest_amt = 0
for i in range(n):
    cat = input("\nEnter category: ")
    amt = float(input("Enter amount in foreign currency: "))
    rate = float(input("Enter exchange rate: "))
    fee_pct = float(input("Enter conversion fee %: "))
    converted = amt * rate
    fee = converted * fee_pct / 100
    final = converted + fee
    print(f"{cat}: INR {final:.2f}")
    total = total + final
    if final > largest_amt:
        largest_amt = final
        largest = cat
print("\n--- Travel Budget Report ---")
print("Total Spending: INR", round(total, 2))
print("Largest Expense:", largest, "- INR", round(largest_amt, 2))
if total <= budget:
    print("Status: Within Budget")
else:
    print("Status: Over Budget by INR", round(total - budget, 2))
