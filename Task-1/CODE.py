
def check_result(marks, pass_mark=35, max_mark=100, grace_limit=5):
    n = len(marks)
    fail_count = 0
    fail_index = -1    
    for i in range(n):
        if marks[i] < pass_mark:
            fail_count += 1
            fail_index = i
    grace_applied = False
    if fail_count == 1:
        deficit = pass_mark - marks[fail_index]
        if deficit <= grace_limit:
            if marks[fail_index] + deficit <= max_mark:
                marks[fail_index] += deficit
                grace_applied = True
                print(f"Grace of {deficit} marks applied in Subject {fail_index+1}")
    final_fail = 0
    for m in marks:
        if m < pass_mark:
            final_fail += 1         
    total = sum(marks)
    percentage = total / n 
    if final_fail == 0:
        if grace_applied:
            result = "PASS WITH GRACE"
        else:
            result = "PASS"
    else:
        result = "FAIL"     
    return total, percentage, result, marks
marks = list(map(int, input("Enter marks of all subjects separated by space: ").split()))
total, per, result, final_marks = check_result(marks)
print("\n--- RESULT ---")
print("Final Marks:", final_marks)
print("Total:", total)
print("Percentage:", per)
print("Result:", result)
