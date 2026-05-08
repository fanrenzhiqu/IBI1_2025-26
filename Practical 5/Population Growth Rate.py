# Pseudocode:
# Create a dictionary to store the 2020 population data for each country.
# Create a dictionary to store the 2024 population data for each country.
# Create an empty dictionary to store the percentage population change for each country.
# For each country in the 2020 population dictionary:
#     Calculate the percentage population change from 2020 to 2024.
#     Store the percentage change in the new dictionary.
#     Print the country name and its percentage change.
# Sort the countries by percentage population change from largest increase to largest decrease.
# Print the sorted population changes.
# Identify the first country in the sorted list as the largest increase.
# Identify the last country in the sorted list as the largest decrease.
# Print the countries with the largest increase and largest decrease.
# Convert the percentage change dictionary into two lists for plotting.
# Create a bar chart showing the population change for each country.
# Add an x-axis label, y-axis label, and title to the bar chart.
# Display the bar chart.

#make dictionary of Population 2020
Population_2020 = {
    "UK" : 66.7,
    "China" : 1426,
    "Italy" : 59.4,
    "Brazil" : 208.6,
    "USA" : 331.6
}

#make dictionary of Population 2024
Population_2024 = {
    "UK" : 69.2,
    "China" : 1410,
    "Italy" : 58.9,
    "Brazil" : 212.0,
    "USA" : 340.1
}

#claculate and print percentage change
Percent_changes = {} #first create a blank dictionary which is used for pairing countries and percentage
for country in Population_2020.keys():
    Percent_change = (Population_2024[country] - Population_2020[country])/Population_2020[country] * 100
    Percent_changes[country] = Percent_change
    print(country, ":", round(Percent_change, 2), "%")


# print the population changes in descending order
sorted_countries = sorted(Percent_changes, key=Percent_changes.get, reverse=True)

print("\nPopulation changes in descending order:")
for country in sorted_countries:
    print(country, ":", round(Percent_changes[country], 2), "%")

# identify the countries with the largest increase and the largest decrease
largest_increase_country = sorted_countries[0]
largest_decrease_country = sorted_countries[-1]

print("\nCountry with the largest increase:", largest_increase_country) #Use the newline character \n for line breaks to make the output more readable.
print("Change:", round(Percent_changes[largest_increase_country], 2), "%")

print("\nCountry with the largest decrease:", largest_decrease_country)
print("Change:", round(Percent_changes[largest_decrease_country], 2), "%")

# Create a well-labelled bar chart
import matplotlib.pyplot as plt

country_names = list(Percent_changes.keys())
change_values = list(Percent_changes.values())

plt.bar(country_names, change_values)
plt.xlabel("Country")
plt.ylabel("Population Change (%)")
plt.title("Population Growth Rate from 2020 to 2024")
plt.show()