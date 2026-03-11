# Ask the user to enter age, weight, gender and creatine concentration
age = int(input("Enter age (years): "))
weight = float(input("Enter weight (kg): "))
gender = input("Enter gender (male/female): ")
cr = float(input("Enter creatine concentration (µmol/L): "))

# Check whether the input values are valid
if age >= 100:
    print("Age needs corrected")

elif weight <= 20 or weight >= 80:
    print("Weight needs corrected")

elif cr <= 0 or cr >= 100:
    print("Creatine concentration needs corrected")

elif gender != "male" and gender != "female":
    print("Gender needs corrected")

else:
    # Calculate creatine clearance
    crcl = ((140 - age) * weight) / (72 * cr)

    # Adjust for female
    if gender == "female":
        crcl = crcl * 0.85

    # Print result
    print("Creatine clearance rate:", crcl)
