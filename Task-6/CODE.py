name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allow = float(input("Enter allowances: "))
ot_hours = float(input("Enter overtime hours: "))
ot_rate = float(input("Enter overtime rate: "))
incentive = float(input("Enter incentive: "))
ot_pay = ot_hours * ot_rate
gross = basic + allow + ot_pay + incentive
pf = basic * 0.12
if gross > 50000:
    tax = gross * 0.10
elif gross > 30000:
    tax = gross * 0.05
else:
    tax = 0
net = gross - pf - tax
print("\n--- Salary Statement ---")
print("Employee:", name)
print("Gross Salary:", gross)
print("PF Deduction:", pf)
print("Tax Deduction:", tax)
print("Net Salary:", net)
