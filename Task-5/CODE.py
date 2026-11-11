name = input("Enter patient name: ")
ptype = input("Enter type (General/Senior/BPL): ").lower()
cons = float(input("Enter consultation charge: "))
diag = float(input("Enter diagnostic charge: "))
treat = float(input("Enter treatment charge: "))
paid = float(input("Enter amount paid: "))
if cons < 0 or diag < 0 or treat < 0:
    print("Invalid Billing")
else:
    total = cons + diag + treat
    if ptype == "senior":
        concession = total * 0.15
    elif ptype == "bpl":
        concession = total * 0.25
    else:
        concession = 0
    final = total - concession
    if paid >= final:
        status = "Settled"
    elif paid > 0:
        status = "Pending"
    else:
        status = "Unpaid"
    print("\n--- Hospital Bill ---")
    print("Patient:", name)
    print("Total:", total)
    print("Concession:", concession)
    print("Final Bill:", final)
    print("Paid:", paid)
    print("Status:", status)
