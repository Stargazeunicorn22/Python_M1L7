x = input("Enter the number of units consumed for electricity: ") 

if int(x) <= 50:
    a = (2.6 * x) + 25
    print("Your electricity bill will be " + str(a) + " rupees.")
elif int(x)<=100:
    a = 175 + (3.25 * (x-50))
    print("Your electricity bill will be " + str(a) + " rupees.")
elif int(x)<=200:
    a = 130 + 162.5 + 45 + (5.26 * (x-100))
    print("Your electricity bill will be " + str(a) + " rupees.")
else:
    a = 130 + 162.5 + 526 + 75 + (8.45 * (x-200))
    print("Your electricity bill will be " + str(a) + " rupees.")