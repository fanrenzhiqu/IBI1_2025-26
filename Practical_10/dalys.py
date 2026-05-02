#These are the exact libraries I will use.
#os for files/directories, pandas for dataframes, matplotlib.pyplot for plotting, and numpy for numerical work.
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Set the working directory and check it
#os.chdir(...) makes Python look in the correct folder
#getcwd() checks where I am
#listdir() checks whether the csv file is actually there
os.chdir("/Users/gongzhenjia/Desktop/IBI_folder/IBI1_2025-26/Practical_10")
print(os.getcwd())
print(os.listdir())

#Read the csv file into a dataframe
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#Inspect the dataframe
#This step helps me confirm:
#the data loaded correctly
#the column names are right
#the data types are sensible
#the year range and DALYs range can be found
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())

#Complete Task 1: show the 3rd and 4th columns for the first 10 rows
#Because Python starts counting from 0:
#3rd column = index 2
#4th column = index 3
first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)
#Then find which of these 10 rows has the largest DALYs:
max_index_first10 = first_10["DALYs"].idxmax()
max_year_first10 = dalys_data.loc[max_index_first10, "Year"]
print(max_year_first10)



#Complete Task 2: use a Boolean to show all years for Zimbabwe
#use a Boolean condition to find the rows where Entity is "Zimbabwe" and then show the Year column
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_years)
#Then find the first and last year:
first_year_zimbabwe = zimbabwe_years.min()
last_year_zimbabwe = zimbabwe_years.max()
print(first_year_zimbabwe)
print(last_year_zimbabwe)



#Complete Task 3: find the countries with the maximum and minimum DALYs in 2019
#create a subset for the most recent year available, 2019, keeping only Entity and DALYs.
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
print(recent_data)
#Then find the rows with maximum and minimum DALYs:
max_row = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row = recent_data.loc[recent_data["DALYs"].idxmin()]
print(max_row)
print(min_row)
#Extract the country names:
max_country = max_row["Entity"]
min_country = min_row["Entity"]
print(max_country)
print(min_country)




#Complete Task 4: plot DALYs over time for one of those two countries
chosen_country = max_country
country_data = dalys_data.loc[dalys_data["Entity"] == chosen_country, ["Year", "DALYs"]]
#Then plot it:
plt.figure(figsize=(10, 5))
plt.plot(country_data["Year"], country_data["DALYs"], 'bo-')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {chosen_country}")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
#Why include all those labels:
#portfolio checklist says all plots must be clearly labelled, 
# and the sheet also discusses plt.xticks(..., rotation=-90) as a way to make the years readable.




#Complete Task 5: Custom Question - Compare DALYs relationship between China and UK
#Question: How has the relationship between the DALYs in China and the UK changed over time? Are they becoming more similar, less similar?
#Line number where analysis starts: 85

#Extract DALYs data for China and UK
china_data = dalys_data.loc[dalys_data["Entity"] == "China", ["Year", "DALYs"]]
uk_data = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["Year", "DALYs"]]

print("China data shape:", china_data.shape)
print("UK data shape:", uk_data.shape)
print("\nChina data:")
print(china_data.head())
print("\nUK data:")
print(uk_data.head())

#Create a merged dataframe for easier comparison
china_uk = china_data.merge(uk_data, on="Year", how="inner", suffixes=("_China", "_UK"))
print("\nMerged data:")
print(china_uk)

#Calculate the absolute difference and relative difference
china_uk["Absolute_Diff"] = abs(china_uk["DALYs_China"] - china_uk["DALYs_UK"])
china_uk["Relative_Diff"] = china_uk["Absolute_Diff"] / china_uk["DALYs_China"]

print("\nDifference analysis:")
print(china_uk[["Year", "Absolute_Diff", "Relative_Diff"]])

#Calculate statistics
print("\nAbsolute difference statistics:")
print(f"Mean: {china_uk['Absolute_Diff'].mean():.2f}")
print(f"Std Dev: {china_uk['Absolute_Diff'].std():.2f}")
print(f"Min year: {china_uk.loc[china_uk['Absolute_Diff'].idxmin(), 'Year']:.0f} (most similar)")
print(f"Max year: {china_uk.loc[china_uk['Absolute_Diff'].idxmax(), 'Year']:.0f} (most different)")

#Plot 1: Time series comparison
plt.figure(figsize=(12, 6))
plt.plot(china_uk["Year"], china_uk["DALYs_China"], 'ro-', label="China", linewidth=2)
plt.plot(china_uk["Year"], china_uk["DALYs_UK"], 'bo-', label="United Kingdom", linewidth=2)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs Comparison: China vs United Kingdom Over Time")
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#Plot 2: Absolute difference over time
plt.figure(figsize=(12, 6))
plt.plot(china_uk["Year"], china_uk["Absolute_Diff"], 'go-', linewidth=2)
plt.xlabel("Year")
plt.ylabel("Absolute Difference in DALYs")
plt.title("Absolute Difference Between China and UK DALYs Over Time")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#Calculate trend in difference
#If the trend is downward, they're becoming more similar; if upward, less similar
first_diff = china_uk["Absolute_Diff"].iloc[0]
last_diff = china_uk["Absolute_Diff"].iloc[-1]
diff_change = last_diff - first_diff
percent_change = (diff_change / first_diff) * 100

print(f"\nTrend analysis:")
print(f"First year ({int(china_uk['Year'].iloc[0])}) absolute difference: {first_diff:.2f}")
print(f"Last year ({int(china_uk['Year'].iloc[-1])}) absolute difference: {last_diff:.2f}")
print(f"Change in difference: {diff_change:.2f} ({percent_change:.2f}%)")
if diff_change < 0:
    print("Result: China and UK are becoming MORE SIMILAR over time")
else:
    print("Result: China and UK are becoming LESS SIMILAR over time")


