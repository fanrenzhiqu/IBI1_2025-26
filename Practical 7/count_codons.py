# Pseudocode:
# 1. Import matplotlib to create the pie chart.
# 2. Define the FASTA file containing yeast cDNA sequences.
# 3. Read the FASTA file:
#    - Store each sequence header and its full DNA sequence.
#    - Join sequence lines that belong to the same gene.
# 4. Ask the user to choose one stop codon: TAA, TAG, or TGA.
# 5. For each gene sequence:
#    - Search for ATG start codons.
#    - From each ATG, read forward in groups of three bases.
#    - Find in-frame stop codons that match the user's chosen stop codon.
#    - If several valid ORFs are found, keep the longest one for that gene.
# 6. Count all codons upstream of the final stop codon.
# 7. Print the codon counts.
# 8. Create and save a labelled pie chart showing codon frequency.

import matplotlib.pyplot as plt

# Input FASTA file containing S. cerevisiae cDNA sequences.
FASTA_FILE = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"


def read_fasta(filename):
    """
    Read a FASTA file and return a list of records.
    Each record is stored as a tuple: (header, sequence).
    """
    records = []
    header = None
    seq_lines = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # Skip empty lines.
            if not line:
                continue

            # A header line marks the start of a new FASTA record.
            if line.startswith(">"):
                # Save the previous record before starting a new one.
                if header is not None:
                    sequence = "".join(seq_lines).upper()
                    records.append((header, sequence))

                header = line[1:]  # Remove the ">" symbol.
                seq_lines = []

            else:
                # Add sequence lines belonging to the current gene.
                seq_lines.append(line)

        # Save the final record after the loop finishes.
        if header is not None:
            sequence = "".join(seq_lines).upper()
            records.append((header, sequence))

    return records


def find_longest_orf_for_stop(sequence, chosen_stop):
    """
    Find the longest possible ORF in one sequence that:
    - starts with ATG
    - ends with the user-selected stop codon
    - has the selected stop codon in-frame

    If there are multiple possible ORFs ending with the chosen stop codon,
    keep the longest one.
    """
    longest_orf = None
    seq_length = len(sequence)

    for start in range(seq_length - 2):
        codon = sequence[start:start + 3]

        # Check whether this position is a possible ORF start.
        if codon == "ATG":

            # Read forward from this ATG in codon-sized steps.
            for i in range(start + 3, seq_length - 2, 3):
                current_codon = sequence[i:i + 3]

                # Only consider stop codons that match the user's choice.
                if current_codon == chosen_stop:
                    orf = sequence[start:i + 3]

                    # Keep the longest ORF found so far.
                    if longest_orf is None or len(orf) > len(longest_orf):
                        longest_orf = orf

    return longest_orf


def count_codons_in_orf(orf_sequence, codon_counts):
    """
    Count codons upstream of the stop codon.
    The final stop codon itself is excluded from the count.
    """
    coding_part = orf_sequence[:-3]

    for i in range(0, len(coding_part), 3):
        codon = coding_part[i:i + 3]

        if len(codon) == 3:
            codon_counts[codon] = codon_counts.get(codon, 0) + 1


def make_pie_chart(codon_counts, chosen_stop):
    """
    Create and save a pie chart showing codon frequency.
    """
    filtered_counts = {
        codon: count
        for codon, count in codon_counts.items()
        if count > 0
    }

    labels = list(filtered_counts.keys())
    sizes = list(filtered_counts.values())

    plt.figure(figsize=(12, 12))

    # Plot codon frequencies as percentages.
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(f"Codon frequency upstream of stop codon {chosen_stop}")
    plt.tight_layout()

    # Save the chart to a PNG file instead of only displaying it.
    output_file = f"codon_frequency_{chosen_stop}.png"
    plt.savefig(output_file, dpi=300)
    plt.close()

    print(f"\nPie chart saved as: {output_file}")


def main():
    """
    Run the codon frequency analysis.
    """
    valid_stops = ["TAA", "TAG", "TGA"]

    # Ask the user to choose one valid stop codon.
    chosen_stop = input("Enter a stop codon (TAA, TAG, or TGA): ").strip().upper()

    while chosen_stop not in valid_stops:
        chosen_stop = input("Invalid input. Please enter TAA, TAG, or TGA: ").strip().upper()

    records = read_fasta(FASTA_FILE)

    codon_counts = {}
    genes_used = 0

    # Analyse only genes that contain a valid ORF ending with the chosen stop codon.
    for header, sequence in records:
        longest_orf = find_longest_orf_for_stop(sequence, chosen_stop)

        if longest_orf is not None:
            genes_used += 1
            count_codons_in_orf(longest_orf, codon_counts)

    if genes_used == 0:
        print(f"No genes with an in-frame {chosen_stop} stop codon were found.")
        return

    print(f"\nGenes containing in-frame {chosen_stop} used for analysis: {genes_used}")
    print("\nCodon counts upstream of the chosen stop codon:")

    for codon in sorted(codon_counts):
        print(f"{codon}: {codon_counts[codon]}")

    make_pie_chart(codon_counts, chosen_stop)


if __name__ == "__main__":
    main()