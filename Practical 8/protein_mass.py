"""
Practical 8: Protein mass predictor.

Pseudocode
1. Store the monoisotopic residue mass for each one-letter amino acid code.
2. Define a function that receives an amino acid sequence.
3. Remove spaces and convert the sequence to upper case.
4. For each amino acid in the sequence:
   - check that it exists in the mass table
   - if it does not exist, return an error message
   - if it does exist, add its mass to the running total
5. Return the total protein mass in atomic mass units (amu).
6. Include an example function call at the bottom of the script.
"""


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


def calculate_protein_mass(sequence):
    """
    Calculate the total mass of a protein sequence.

    The input should be a string of one-letter amino acid codes.
    The function returns the total mass as a float when the sequence is valid.
    If the sequence contains an unknown amino acid, an error message is returned.
    """
    sequence = sequence.replace(" ", "").upper()
    total_mass = 0

    if sequence == "":
        return "Error: no amino acid sequence was supplied."

    for amino_acid in sequence:
        if amino_acid not in AMINO_ACID_MASSES:
            return f"Error: amino acid '{amino_acid}' has no recorded mass."

        total_mass += AMINO_ACID_MASSES[amino_acid]

    return round(total_mass, 2)


def protein_mass(sequence):
    """
    Wrapper function with a short name for easy marking/testing.
    """
    return calculate_protein_mass(sequence)


if __name__ == "__main__":
    example_sequence = "MKWVTF"
    example_mass = calculate_protein_mass(example_sequence)

    print("Example amino acid sequence:", example_sequence)
    print("Protein mass:", example_mass, "amu")
