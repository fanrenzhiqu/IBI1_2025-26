# Pseudocode:
# Create a list of resting heart rates.
# Count how many patients are in the dataset.
# Calculate the mean heart rate.
# Print the number of patients and the mean heart rate.
# Set the count of Low, Normal, and High heart rate categories to 0.
# For each heart rate in the list:
#     If the heart rate is less than 60, add 1 to the Low category.
#     If the heart rate is between 60 and 120, add 1 to the Normal category.
#     If the heart rate is greater than 120, add 1 to the High category.
# Print the number of patients in each heart rate category.
# Compare the three category counts.
# Print which category contains the largest number of patients.
# Create a pie chart using the three category counts.
# Add labels and a title to the pie chart.
# Display the pie chart.

# 1. number of patients and mean heart rate
heart_rate = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rate)
mean_heart_rate = sum(heart_rate)/num_patients
print(f"there are {num_patients} patients in the dataset and mean heart value of the dataset is {mean_heart_rate:.2f}bpm.")

# 2. count each category
low_num = 0
normal_num = 0
high_num = 0
for rate in heart_rate:
	if rate < 60:
		low_num += 1
	elif 60 <= rate <= 120:
		normal_num += 1
	else:
		high_num +=1

print(f"Low heart rate patients: {low_num}")
print(f"Normal heart rate patients: {normal_num}")
print(f"High heart rate patients: {high_num}")

# 3. identify the largest category
if low_num > normal_num and low_num > high_num:
    print("The Low category contains the largest number of patients.")
elif normal_num > low_num and normal_num > high_num:
    print("The Normal category contains the largest number of patients.")
elif high_num > low_num and high_num > normal_num:
    print("The High category contains the largest number of patients.")
else:
    print("There is a tie for the largest category.")

# 4. pie chart
import matplotlib.pyplot as plt

categories = ["Low", "Normal", "High"]
counts = [low_num, normal_num, high_num]

plt.pie(counts, labels=categories, autopct="%1.1f%%")
plt.title("Distribution of Heart Rate Categories")
plt.show()
