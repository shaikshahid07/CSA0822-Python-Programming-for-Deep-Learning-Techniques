def check_result(marks):
    if marks >= 50:
        return "Passed"
    else:
        return "Failed"
marks = int(input("Enter the student's marks: "))
result = check_result(marks)
print("Result:", result)
