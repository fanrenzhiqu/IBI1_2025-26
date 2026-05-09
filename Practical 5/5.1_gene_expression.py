# Pseudocode:
# Create a dictionary to store gene names and their expression values.
# Print the original gene expression dictionary.
# Add MYC and its expression value to the dictionary.
# Print the updated dictionary.
# Convert the dictionary keys and values into two lists for plotting.
# Create a bar chart showing the expression values of all genes.
# Add a title, x-axis label, and y-axis label to the bar chart.
# Set a gene of interest that can be changed in the script.
# Check whether the selected gene is in the dictionary.
# If the selected gene is present, print its expression value.
# If the selected gene is not present, print an error message.
# Calculate the average expression value across all genes.
# Print the average gene expression level.


gene_expression = {
"TP53" : 12.4,
"EGFR" : 15.1,
"BRCA1" : 8.2,
"PTEN" : 5.3,
"ESR1" : 10.7
}

print(gene_expression)

#add MYC
gene_expression["MYC"] = 11.6
print(gene_expression)

#make bar chart
#turn the dictionary into two lists
genes = list(gene_expression.keys())
values = list(gene_expression.values())
import matplotlib.pyplot as plt
plt.bar(genes, values)
#make it “well-labelled”
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Value")
plt.show()

# Select one gene of interest
# This value can be changed to test different genes
# Example: "ESR1", "TP53", "MYC", or a gene not in the dataset

gene_of_interest = "ESR1"

# Check whether the selected gene is present in the dictionary
# If it is present, print its expression value
# If it is not present, print an informative error message

if gene_of_interest in gene_expression:
    print(f"The expression value of {gene_of_interest} is {gene_expression[gene_of_interest]}")
else:
    print(f"Error: {gene_of_interest} is not present in the dataset.")




# Calculate the average of all gene expression values
average_expression = sum(gene_expression.values()) / len(gene_expression)

# Print the average gene expression level
print(f"The average gene expression level is {average_expression:.2f}")
