def calculate_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    elif units <= 300:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    else:
        bill = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 9
    bill = bill + 100
    surcharge = 0
    if bill > 1000:
        surcharge = bill * 0.10
        bill = bill + surcharge
    rebate = 0
    if units < 100:
        rebate = bill * 0.05
        bill = bill - rebate
    return bill, surcharge, rebate
print("=== Progressive Electricity Billing System ===")
months = int(input("Enter number of months: "))
prev_bill = None
total_all = 0
print("\nMonth | Units | Bill | Status")
print("----------------------------------")
for i in range(1, months + 1):
    units = int(input(f"\nEnter units for Month {i}: "))
    bill, surcharge, rebate = calculate_bill(units)
    total_all += bill
    if prev_bill is None:
        status = "First Month"
    elif bill > prev_bill * 1.30:
        status = "Unusual Increase!"
    else:
        status = "Normal"
    print(f"Month {i} | Units: {units} | Bill: Rs.{bill:.2f} | {status}")
    if surcharge > 0:
        print(f"  -> Surcharge Applied: Rs.{surcharge:.2f}")
    if rebate > 0:
        print(f"  -> Rebate Applied: Rs.{rebate:.2f}")
    prev_bill = bill
print("\n----------------------------------")
print(f"Total Bill for {months} months: Rs.{total_all:.2f}")
print(f"Average Monthly Bill: Rs.{total_all/months:.2f}")
