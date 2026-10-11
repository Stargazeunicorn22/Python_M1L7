print("Select your ride:")
print("1. Bike")
print("2. Car")
a = input("Enter your preference;; 1 or 2: ")
if int(a) == 1:
    print("You like bikes!")
    print("Here are your options: ")
    print("1. Red")
    print("2. Blue")
    x = input("Enter your preference; 1 or 2: ")
    if int(x) == 1:
        print("Here is your red bike.")
    else:
        print("Here is your blue bike.")
else:
    print("You like cars!")
    print("Here are your options: ")
    print("1. Red")
    print("2. Blue")
    x = input("Enter your preference; 1 or 2: ")
    if int(x) == 1:
        print("Here is your red car.")
    else:
        print("Here is your blue car.")