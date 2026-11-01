
venue = int(input("Venue cost: "))
equipment = int(input("Equipment cost: "))
transport = int(input("Transport cost: "))
catering = int(input("Catering per person: "))
certificate = int(input("Certificate per person: "))
fee = int(input("Registration fee per person: "))
sponsorship = int(input("Sponsorship: "))
n = int(input("No. of participants: "))
fixed = venue + equipment + transport
per_person = catering + certificate
total_cost = fixed + per_person * n
total_income = sponsorship + fee * n
contribution = fee * n
shortfall = total_cost - total_income
if shortfall < 0:
    shortfall = 0
break_even = (fixed - sponsorship) / (fee - per_person)
print("\n--- RESULT ---")
print("Total Cost:", total_cost)
print("Total Income:", total_income)
print("Participant Contribution:", contribution)
print("Shortfall:", shortfall)
print("Min. Registration to Break Even:", int(break_even)+1)
