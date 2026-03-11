age = int(input("Enter age (years): "))
if age >= 100:
    print("Age needs corrected")
    exit()

weight = float(input("Enter weight (kg): "))
if weight <= 20 or weight >= 80:
    print("Weight needs corrected")
    exit()

gender = input("Enter gender (male/female): ").lower()
if gender != "male" and gender != "female":
    print("Gender needs corrected")
    exit()

cr = float(input("Enter creatine concentration (µmol/L): "))
if cr <= 0 or cr >= 100:
    print("Creatine concentration needs corrected")
    exit()

crcl = ((140 - age) * weight) / (72 * cr)

if gender == "female":
    crcl = crcl * 0.85

print("Creatine clearance rate:", crcl)
