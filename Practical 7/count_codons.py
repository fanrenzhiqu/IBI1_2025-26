import matplotlib.pyplot as plt

FASTA_FILE = "Saccharomyces_cerevisiae.R64-1-1.cdna.all (1).fa"


def read_fasta(filename):
    """
    Read a FASTA file and return a list of tuples:
    [(header, sequence), ...]
    """
    records = []
    header = None # We first create a variable named `header`, and set it equal to `None` initially. 
    #The meaning of `None` here is: No content yet / We have not yet read the header
    seq_lines = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip() # Clean up line by stripping whitespace
            if not line:
                continue

            if line.startswith(">"):
                if header is not None:
                    sequence = "".join(seq_lines).upper() #Concatenate (join) all text elements in seq_lines into ONE single continuous string. And convert every character in the new concatenated string to UPPERCASE letters
                    records.append((header, sequence))
                header = line[1:]   # remove ">"
                seq_lines = []
            else:
                seq_lines.append(line)

        # save the last record
        if header is not None:
            sequence = "".join(seq_lines).upper()
            records.append((header, sequence))

    return records


def get_gene_name(header):
    """
    Try to extract gene name from FASTA header.
    Example header may contain: gene:XYZ
    If not found, use the first word in header.
    """
    parts = header.split()

    for part in parts:
        if part.startswith("gene:"):
            return part.split("gene:")[1]

    return parts[0]


def find_longest_orf_for_stop(sequence, chosen_stop): #It needs two inputs
    """
    Find the longest ORF in one sequence that:
    - starts with ATG
    - ends with the chosen stop codon
    - stop codon is in-frame

    Return the ORF sequence including ATG and stop codon.
    If no valid ORF exists, return None.
    """
    longest_orf = None

    seq_length = len(sequence)

    for start in range(seq_length - 2): #Each codon needs 3 letters, so it is "seq_length - 2"
        codon = sequence[start:start + 3]

        if codon == "ATG":
            # move in-frame from this ATG
            for i in range(start + 3, seq_length - 2, 3):
                current_codon = sequence[i:i + 3]

                if current_codon == chosen_stop:
                    orf = sequence[start:i + 3]  # include stop codon

                    if (longest_orf is None) or (len(orf) > len(longest_orf)):
                        longest_orf = orf

    return longest_orf


def count_codons_in_orf(orf_sequence, codon_counts):
    """
    Count all codons upstream of the stop codon.
    So we do NOT count the final stop codon itself.
    """
    # exclude final stop codon
    coding_part = orf_sequence[:-3]

    for i in range(0, len(coding_part), 3):
        codon = coding_part[i:i + 3]
        if len(codon) == 3:
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1


def make_pie_chart(codon_counts, chosen_stop):
    """
    Create and save pie chart to a file.
    """
    # remove codons with 0 count
    filtered_counts = {codon: count for codon, count in codon_counts.items() if count > 0}

    labels = list(filtered_counts.keys())
    sizes = list(filtered_counts.values())

    plt.figure(figsize=(12, 12))
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title(f"Codon frequency upstream of stop codon {chosen_stop}")
    plt.tight_layout()

    output_file = f"codon_frequency_{chosen_stop}.png"
    plt.savefig(output_file, dpi=300)
    plt.close()

    print(f"\nPie chart saved as: {output_file}")


def main():
    valid_stops = ["TAA", "TAG", "TGA"]

    chosen_stop = input("Enter a stop codon (TAA, TAG, or TGA): ").strip().upper()

    while chosen_stop not in valid_stops:
        chosen_stop = input("Invalid input. Please enter TAA, TAG, or TGA: ").strip().upper()

    records = read_fasta(FASTA_FILE)

    codon_counts = {}
    genes_used = 0

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