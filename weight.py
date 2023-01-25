weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ").upper()

if unit == "K":
    print("Weight in Lbs: ", (2.205*weight), "lbs")
elif unit == "L":
    print("Weight in Kgs: ", (0.454*weight),"Kgs")
else:
    print("Please enter a valid input")
    