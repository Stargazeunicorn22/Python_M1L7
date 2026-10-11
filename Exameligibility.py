student = input("Enter your attendence score: ")
med = input ("Do you have a medical cause? 'Y' or 'N': ")
if med == 'Y':
    print ("You may take the exam.")
else:
    if float(student) >= 75:
        print("You may take the exam.")
    else:
        print("Your attendence score is too low. You can't take the exam.")