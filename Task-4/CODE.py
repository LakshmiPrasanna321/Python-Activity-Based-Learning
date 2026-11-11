n = int(input("Enter number of students: "))
eligible = []
for i in range(n):
    name = input("Enter name: ")
    marks = list(map(int, input("Enter 3 subject marks separated by space: ").split()))
    att = float(input("Enter attendance %: "))
    income = int(input("Enter family income: "))
    agg = sum(marks) / len(marks)
    if agg >= 75 and min(marks) >= 40 and att >= 75 and income <= 300000:
        eligible.append((name, agg, att))
    else:
        print(name, "Not Eligible")
eligible.sort(key=lambda x: (-x[1], -x[2], x[0]))
print("\nRanked Eligible Students:")
for rank, (name, agg, att) in enumerate(eligible, 1):
    print(f"{rank}. {name} - Aggregate: {agg:.2f}%, Attendance: {att}%")
