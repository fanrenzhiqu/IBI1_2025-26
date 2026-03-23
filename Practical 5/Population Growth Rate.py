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

# create a well-labelled bar chart
import matplotlib.pyplot as plt

country_names = list(Percent_changes.keys())
change_values = list(Percent_changes.values())

plt.bar(country_names, change_values)
plt.xlabel("Country")
plt.ylabel("Population Change (%)")
plt.title("Population Growth Rate from 2020 to 2024")
plt.show()