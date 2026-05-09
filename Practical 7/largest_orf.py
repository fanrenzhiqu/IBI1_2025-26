#Pseudocode:
#Define the RNA sequence and stop codons.
#Create an empty list for ORFs.
#Scan the RNA sequence for AUG start codons.
#For each AUG found:
#    Read codons forward in groups of three.
#    If a stop codon is found:
#        Save the sequence from AUG to the stop codon as an ORF.
#        Stop reading this ORF.
#If ORFs are found:
#    Find and print the longest ORF and its length.
#Else:
#    Print "No ORF found".



# Create the RNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# Create a list of stop codons
stop_codons = ['UAA', 'UAG', 'UGA']

# Create an empty list to store all ORFs
all_orfs = []

# Look through every position in the sequence
for i in range(len(seq) - 2):
    # Take 3 nucleotides from the current position
    start_codon = seq[i:i+3]

    # Check whether the current codon is AUG
    if start_codon == 'AUG':

        # From this AUG, read forward in groups of 3
        for j in range(i + 3, len(seq) - 2, 3):
            # Take the next codon
            stop_codon = seq[j:j+3]

            # Check whether this codon is a stop codon
            if stop_codon in stop_codons:
                # Save the ORF from AUG to the stop codon
                orf = seq[i:j+3]
                all_orfs.append(orf)

                # Stop at the first stop codon
                break

# Check whether any ORF was found
if all_orfs:
    # Find the longest ORF
    largest_orf = max(all_orfs, key=len)

    # Print all ORFs, the largest ORF, and its length
    print("All ORFs found:", all_orfs)
    print("The largest ORF is", largest_orf)
    print("The length is", len(largest_orf), "nucleotides")
else:
    # Print a message if no ORF is found
    print("No ORF found")
