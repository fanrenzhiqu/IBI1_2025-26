# Pseudocode:
# 1. Define input and output file names
# 2. Define the list of stop codons (TAA, TAG, TGA)
# 3. Define a function to find stop codons in a sequence:
#    - Check if sequence starts with ATG (start codon)
#    - Iterate through the sequence in steps of 3 (codons)
#    - If a codon matches a stop codon, add it to the list
#    - Return the list of found stop codons
# 4. Define a function to write a sequence to the output file:
#    - Create header with gene name and found stop codons
#    - Write the sequence in lines of 60 characters each
# 5. Open input and output files
# 6. Initialize variables for gene name and sequence
# 7. Read the input file line by line:
#    - If line starts with '>', it's a header: extract gene name
#    - Else, append to sequence
#    - If next line is header or end of file, process the current sequence:
#      - Find stop codons in the sequence
#      - If stop codons found, write to output file
#      - Reset sequence for next gene
# 8. Close files (handled by 'with' statement)


# This script reads a FASTA file, finds genes with at least one in-frame
# stop codon (TAA, TAG, TGA), and writes them to a new FASTA file.

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

stop_codons = ["TAA", "TAG", "TGA"]


def find_stop_codons(sequence):
    """
    Find all in-frame stop codons in a DNA sequence.

    Args:
        sequence (str): The DNA sequence to analyze.

    Returns:
        list: List of stop codons found in the sequence.
    """
    found = []

    # ORF must begin with ATG (start codon)
    if not sequence.startswith("ATG"):
        return found

    # Read codons in frame: positions 0, 3, 6, 9...
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in stop_codons:
            found.append(codon)

    return found


def write_sequence(outfile, gene_name, sequence, found_stops):
    """
    Write a gene sequence to the output FASTA file with stop codons in header.

    Args:
        outfile (file object): The output file to write to.
        gene_name (str): The name of the gene.
        sequence (str): The DNA sequence.
        found_stops (list): List of stop codons found.
    """
    # Write header line with gene name and stop codons
    header = ">" + gene_name + "," + ",".join(found_stops) + "\n"
    outfile.write(header)

    # Write sequence in lines of 60 bases each
    for i in range(0, len(sequence), 60):
        outfile.write(sequence[i:i+60] + "\n")


# Open input and output files using 'with' for automatic closing
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    gene_name = ""
    sequence = ""

    for line in infile:
        # Remove trailing newline
        line = line.strip()

        if line.startswith(">"):
            # Process previous gene if sequence exists
            if sequence:
                found_stops = find_stop_codons(sequence)
                if found_stops:
                    write_sequence(outfile, gene_name, sequence, found_stops)
                sequence = ""  # Reset for next gene

            # Extract gene name from header (remove '>')
            gene_name = line[1:]
        else:
            # Append sequence line
            sequence += line

    # Process the last gene after loop ends
    if sequence:
        found_stops = find_stop_codons(sequence)
        if found_stops:
            write_sequence(outfile, gene_name, sequence, found_stops)

        if line.startswith(">"):
            # Process the previous gene before starting a new one
            if gene_name != "":
                found_stops = find_stop_codons(sequence)
                if len(found_stops) > 0:
                    write_sequence(outfile, gene_name, sequence, found_stops)

            # Start a new gene
            gene_name = line[1:].split()[0]
            sequence = ""

        else:
            #line.upper() means converting the line to uppercase.
            sequence += line.upper()

    # Process the last gene in the file
    if gene_name != "":
        found_stops = find_stop_codons(sequence)
        if len(found_stops) > 0:
            write_sequence(outfile, gene_name, sequence, found_stops)

print("Finished! Results written to", output_file)