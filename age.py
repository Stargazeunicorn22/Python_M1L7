age = int(input("Enter student's age: "))
if age >= 10:
    if age <= 20:
        print("Enrollment successful! Student is allowed in grade 10.")
    else:
        print("Enrollment failed: Student whose age is more than 20 cannot enrol.")
else:
    print("Enrollment failed: Student is under 10 years old.")