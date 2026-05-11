"""
stop_codons.py

Pseudocode:
1. Define the input FASTA file and the output FASTA file.
2. Define the three stop codons: TAA, TAG and TGA.
3. Read the original FASTA file gene by gene.
4. For each gene:
   - Extract only the gene name from the FASTA header.
   - Join all sequence lines into one complete sequence.
   - Check which of the three stop codons are present at least once.
5. If at least one stop codon is found:
   - Write the gene to stop_genes.fa.
   - The new sequence name contains only the gene name and the stop codons found.
6. Write the sequence in lines of 60 bases.
"""


input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

stop_codons = ["TAA", "TAG", "TGA"]


def get_gene_name(header_line):
    """
    Extract only the gene name from a FASTA header.

    Example:
        >GENE1 some extra description
    becomes:
        GENE1
    """
    return header_line[1:].split()[0]


def find_present_stop_codons(sequence):
    """
    Check which stop codons are present at least once as real codons.

    The sequence is checked in groups of three bases.
    Each stop codon is recorded only once, even if it appears many times.
    """
    sequence = sequence.upper()

    found_stops = []

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]

        if codon in stop_codons and codon not in found_stops:
            found_stops.append(codon)

    return found_stops


def write_fasta_record(outfile, gene_name, sequence, found_stops):
    """
    Write one FASTA record to the output file.

    The header contains only:
    - the gene name
    - the stop codons found in that gene
    """
    header = ">" + gene_name + "_" + "_".join(found_stops)
    outfile.write(header + "\n")

    for i in range(0, len(sequence), 60):
        outfile.write(sequence[i:i + 60] + "\n")


def process_gene(outfile, gene_name, sequence_lines):
    """
    Process one gene sequence and write it to the output file
    if it contains at least one stop codon.
    """
    if gene_name == "" or len(sequence_lines) == 0:
        return

    sequence = "".join(sequence_lines).upper()
    found_stops = find_present_stop_codons(sequence)

    if len(found_stops) > 0:
        write_fasta_record(outfile, gene_name, sequence, found_stops)


with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    gene_name = ""
    sequence_lines = []

    for line in infile:
        line = line.strip()

        if line == "":
            continue

        if line.startswith(">"):
            # Process the previous gene before starting a new one
            process_gene(outfile, gene_name, sequence_lines)

            # Start a new gene
            gene_name = get_gene_name(line)
            sequence_lines = []

        else:
            sequence_lines.append(line)

    # Process the final gene in the file
    process_gene(outfile, gene_name, sequence_lines)


print("Finished! Results written to", output_file)