need_data = float(input("Enter data needed (GB): "))
need_validity = int(input("Enter validity needed (days): "))
budget = float(input("Enter budget: "))
n = int(input("Enter number of plans: "))
best = ""
best_cost = 999999
for i in range(n):
    print(f"\nPlan {i+1}:")
    pname = input("Enter plan name: ")
    cost = float(input("Enter plan cost: "))
    data = float(input("Enter plan data (GB): "))
    validity = int(input("Enter plan validity (days): "))
    if validity >= need_validity and cost <= budget:
        if need_data > data:
            excess = (need_data - data) * 20
        else:
            excess = 0
        total = cost + excess
        print("Total Cost:", total)
        if total < best_cost:
            best_cost = total
            best = pname
    else:
        print("Not Eligible")
if best != "":
    print("\nBest Plan:", best)
    print("Best Cost:", best_cost)
else:
    print("\nNo eligible plan found")
