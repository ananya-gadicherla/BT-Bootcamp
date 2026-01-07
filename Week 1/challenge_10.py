def student_report_card(name, score1, score2, score3):
    # Calculate total and average
    total = score1 + score2 + score3
    average = total / 3

    # Determine class
    if average >= 60:
        student_class = "1st Class"
    elif average >= 50:
        student_class = "2nd Class"
    elif average >= 35:
        student_class = "Pass Class"
    else:
        student_class = "Fail"

    
    print(f"Student Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Class Secured: {student_class}")

student_name = input("Enter your name : ")
marks1 = float(input("Enter marks1 : "))

marks2 = float(input("Enter marks2 : "))
marks3 = float(input("Enter marks3 : "))
student_report_card(student_name, marks1, marks2, marks3)


