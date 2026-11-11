dist = int(input("Enter distance (km): "))
cls = input("Enter class (Sleeper/AC): ").lower()
n = int(input("Enter number of passengers: "))
if cls == "sleeper":
    rate = 1
else:
    rate = 2
base = dist * rate
total = 0
for i in range(n):
    age = int(input(f"Enter age of passenger {i+1}: "))
    if age < 5:
        fare = 0
    elif age >= 60:
        fare = base * 0.5
    else:
        fare = base
    fare = fare + 50
    total = total + fare
    print(f"Passenger {i+1} Fare: {fare}")
cancel = input("Cancelled? (yes/no): ").lower()
if cancel == "yes":
    total = total * 0.75
    print("25% cancellation penalty applied")
print("Total Fare:", total)
