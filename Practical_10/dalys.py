# Pseudocode for Practical 10:
#
# 1. Import the required libraries.
# 2. Read the DALYs csv file from the same folder as this script.
# 3. Inspect the dataframe using head(), info(), and describe().
# 4. Show the 3rd and 4th columns for the first 10 rows, then identify the year
#    with the maximum DALYs in those rows.
# 5. Use a Boolean condition to show all years recorded for Zimbabwe.
# 6. Find the countries with the maximum and minimum DALYs in 2019.
# 7. Plot DALYs over time for one of those countries.
# 8. Answer the question in question.txt by comparing DALYs in China and the UK.
# 9. Clearly label all plots.

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------
# Load the dataset
# -----------------------------

# Use the folder where this script is stored.
# This avoids using a personal absolute path that only works on one computer.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(SCRIPT_DIR, "dalys-rate-from-all-causes.csv")
dalys_data = pd.read_csv(csv_path)


# -----------------------------
# Inspect the dataframe
# -----------------------------

print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())


# -----------------------------
# Task 1: Show Year and DALYs for the first 10 rows
# -----------------------------

# Python counts from 0, so columns 2 and 3 are the 3rd and 4th columns.
first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)

max_index_first10 = first_10["DALYs"].idxmax()
max_year_first10 = dalys_data.loc[max_index_first10, "Year"]
print(max_year_first10)

# Answer comment: In the first 10 years recorded for Afghanistan,
# the maximum DALYs occurred in 1998.


# -----------------------------
# Task 2: Use a Boolean to show all years for Zimbabwe
# -----------------------------

zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_years)

first_year_zimbabwe = zimbabwe_years.min()
last_year_zimbabwe = zimbabwe_years.max()

print(first_year_zimbabwe)
print(last_year_zimbabwe)

# Answer comment: For Zimbabwe, DALYs were recorded from 1990 to 2019.


# -----------------------------
# Task 3: Find maximum and minimum DALYs in 2019
# -----------------------------

recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_row = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row = recent_data.loc[recent_data["DALYs"].idxmin()]

max_country = max_row["Entity"]
min_country = min_row["Entity"]

print(max_row)
print(min_row)
print(max_country)
print(min_country)

# Answer comment: In 2019, the country with the maximum DALYs was Lesotho.
# In 2019, the country with the minimum DALYs was Singapore.


# -----------------------------
# Task 4: Plot DALYs over time for one identified country
# -----------------------------

chosen_country = max_country
country_data = dalys_data.loc[
    dalys_data["Entity"] == chosen_country,
    ["Year", "DALYs"]
]

plt.figure(figsize=(10, 5))
plt.plot(country_data["Year"], country_data["DALYs"], "bo-")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {chosen_country}")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, "lesotho_dalys_over_time.png"))
plt.show()


# -----------------------------
# Task 5: Custom question from question.txt
# -----------------------------

# Question:
# How has the relationship between the DALYs in China and the UK changed over time?
# Are they becoming more similar, less similar?

# This code interprets "relationship" as the DALYs gap between China and the UK.
# A smaller absolute difference means the two countries are becoming more similar.

china_data = dalys_data.loc[
    dalys_data["Entity"] == "China",
    ["Year", "DALYs"]
]

uk_data = dalys_data.loc[
    dalys_data["Entity"] == "United Kingdom",
    ["Year", "DALYs"]
]

china_uk = (
    china_data.merge(uk_data, on="Year", how="inner", suffixes=("_China", "_UK"))
    .sort_values("Year")
    .reset_index(drop=True)
)

china_uk["Absolute_Diff"] = abs(china_uk["DALYs_China"] - china_uk["DALYs_UK"])

china_uk["Relative_Diff"] = (
    2 * china_uk["Absolute_Diff"] /
    (china_uk["DALYs_China"] + china_uk["DALYs_UK"])
)

print("\nChina vs United Kingdom DALYs comparison")
print(f"Years compared: {china_uk['Year'].min()} to {china_uk['Year'].max()}")
print(f"Number of years: {len(china_uk)}")
print(f"Mean absolute difference: {china_uk['Absolute_Diff'].mean():.2f}")
print(f"Mean relative difference: {china_uk['Relative_Diff'].mean():.3f}")

most_similar_index = china_uk["Absolute_Diff"].idxmin()
most_different_index = china_uk["Absolute_Diff"].idxmax()

print(
    f"Most similar year: {int(china_uk.loc[most_similar_index, 'Year'])}, "
    f"difference = {china_uk.loc[most_similar_index, 'Absolute_Diff']:.2f}"
)

print(
    f"Most different year: {int(china_uk.loc[most_different_index, 'Year'])}, "
    f"difference = {china_uk.loc[most_different_index, 'Absolute_Diff']:.2f}"
)


# Plot 1: Compare China and UK DALYs over time.
plt.figure(figsize=(12, 6))
plt.plot(
    china_uk["Year"],
    china_uk["DALYs_China"],
    "ro-",
    label="China",
    linewidth=2
)
plt.plot(
    china_uk["Year"],
    china_uk["DALYs_UK"],
    "bo-",
    label="United Kingdom",
    linewidth=2
)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs Comparison: China vs United Kingdom Over Time")
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, "china_uk_dalys_comparison.png"))
plt.show()


# Plot 2: Show whether the DALYs gap is narrowing or widening.
plt.figure(figsize=(12, 6))
plt.plot(china_uk["Year"], china_uk["Absolute_Diff"], "go-", linewidth=2)
plt.xlabel("Year")
plt.ylabel("Absolute Difference in DALYs")
plt.title("Absolute Difference Between China and UK DALYs Over Time")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, "china_uk_dalys_difference.png"))
plt.show()


# Use first/last comparison and a linear trend to describe the change.
first_diff = china_uk["Absolute_Diff"].iloc[0]
last_diff = china_uk["Absolute_Diff"].iloc[-1]

diff_change = last_diff - first_diff
percent_change = (diff_change / first_diff) * 100

slope, intercept = np.polyfit(china_uk["Year"], china_uk["Absolute_Diff"], 1)

print("\nTrend analysis:")
print(f"First year ({int(china_uk['Year'].iloc[0])}) absolute difference: {first_diff:.2f}")
print(f"Last year ({int(china_uk['Year'].iloc[-1])}) absolute difference: {last_diff:.2f}")
print(f"Change in difference: {diff_change:.2f} ({percent_change:.2f}%)")
print(f"Linear trend slope: {slope:.2f}")

if slope < 0:
    print("Conclusion: The DALYs gap between China and the UK narrowed over time.")
    print("Therefore, the two countries became more similar in terms of DALYs.")
elif slope > 0:
    print("Conclusion: The DALYs gap between China and the UK widened over time.")
    print("Therefore, the two countries became less similar in terms of DALYs.")
else:
    print("Conclusion: The DALYs gap between China and the UK was stable over time.")


# Final answer comment:
# The absolute difference decreased from 13997.38 in 1990 to 1313.90 in 2019.
# The linear trend slope was -458.83.
# Therefore, the DALYs gap between China and the United Kingdom narrowed over time,
# meaning that the two countries became more similar in terms of DALYs.