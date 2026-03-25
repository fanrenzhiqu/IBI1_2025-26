# Pseudocode:
# Ask the user to enter age
# If age is not less than 100, print that age needs corrected and stop
# Ask the user to enter weight
# If weight is not more than 20 and less than 80, print that weight needs corrected and stop
# Ask the user to enter gender
# If gender is not male or female, print that gender needs corrected and stop
# Ask the user to enter creatine concentration
# If creatine concentration is not more than 0 and less than 100, print that creatine concentration needs corrected and stop
# Calculate creatine clearance rate using the Cockcroft-Gault equation
# If gender is female, multiply the result by 0.85
# Print the creatine clearance rate

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
