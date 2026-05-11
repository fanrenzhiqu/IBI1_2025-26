"""
Practical 8: Protein mass predictor.

Pseudocode
1. Store the monoisotopic residue mass for each one-letter amino acid code.
2. Define a function that receives an amino acid sequence.
3. Check that the input is a string.
4. Remove whitespace and convert the sequence to upper case.
5. Check that the sequence is not empty.
6. For each amino acid in the sequence:
   - check whether the amino acid has a recorded mass in the table
   - if it does not, return an error message
   - if it does, add its mass to the running total
7. Return the total protein mass in atomic mass units (amu).
8. Include an example function call at the bottom of the script.
"""


# Dictionary storing the monoisotopic residue mass for each amino acid.
# The keys are one-letter amino acid codes and the values are masses in amu.
AMINO_ACID_MASSES = {
    "G": 57.02,   # Glycine
    "A": 71.04,   # Alanine
    "S": 87.03,   # Serine
    "P": 97.05,   # Proline
    "V": 99.07,   # Valine
    "T": 101.05,  # Threonine
    "C": 103.01,  # Cysteine
    "I": 113.08,  # Isoleucine
    "L": 113.08,  # Leucine
    "N": 114.04,  # Asparagine
    "D": 115.03,  # Aspartic acid
    "Q": 128.06,  # Glutamine
    "K": 128.09,  # Lysine
    "E": 129.04,  # Glutamic acid
    "M": 131.04,  # Methionine
    "H": 137.06,  # Histidine
    "F": 147.07,  # Phenylalanine
    "R": 156.10,  # Arginine
    "Y": 163.06,  # Tyrosine
    "W": 186.08,  # Tryptophan
}


def protein_mass(sequence):
    """
    Calculate the total mass of a protein sequence.

    The input should be a string containing one-letter amino acid codes.
    The function returns the total protein mass as a float if the sequence is valid.
    If the sequence is empty or contains an unknown amino acid, an error message is returned.
    """

    # Check that the input is a string before processing it.
    if not isinstance(sequence, str):
        return "Error: sequence must be supplied as a string."

    # Remove all whitespace and allow lower-case input by converting to upper case.
    sequence = "".join(sequence.split()).upper()

    # Check that the user has supplied at least one amino acid.
    if sequence == "":
        return "Error: no amino acid sequence was supplied."

    # Start with a mass of zero before adding each residue mass.
    total_mass = 0

    # Check each amino acid and add its mass to the total.
    for amino_acid in sequence:
        if amino_acid not in AMINO_ACID_MASSES:
            return f"Error: amino acid '{amino_acid}' has no recorded mass."

        total_mass += AMINO_ACID_MASSES[amino_acid]

    # Return the final protein mass rounded to two decimal places.
    return round(total_mass, 2)


# Example function call.
if __name__ == "__main__":
    example_sequence = "MKWVTF"
    example_mass = protein_mass(example_sequence)

    print("Example amino acid sequence:", example_sequence)
    print("Protein mass:", example_mass, "amu")