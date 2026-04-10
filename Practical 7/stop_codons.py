
# This script reads a FASTA file, finds genes with at least one in-frame
# stop codon (TAA, TAG, TGA), and writes them to a new FASTA file.

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all (1).fa"
output_file = "stop_genes.fa"

stop_codons = ["TAA", "TAG", "TGA"]


def find_stop_codons(sequence):  #定义一个函数（function），这个函数名字叫 find_stop_codons，它要接收一个输入，叫 sequence
#定义函数时，后面括号里的东西，表示这个函数将来要接收的输入。
    found = []

    # ORF must begin with ATG
    if not sequence.startswith("ATG"):
        return found

    # Read codons in frame: 0, 3, 6, 9...
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in stop_codons :
            found.append(codon)

    return found


def write_sequence(outfile, gene_name, sequence, found_stops):
    # Write header line, join() is used to join multiple strings from a list together using a given separator.
    header = ">" + gene_name + "," + ",".join(found_stops) + "\n" 
    #Write the constructed header to the output file.
    outfile.write(header)

    # Write sequence in several lines (60 bases per line)
    for i in range(0, len(sequence), 60):
        outfile.write(sequence[i:i+60] + "\n")


#The with ... as ... statement in Python safely opens resources (such as files) and automatically closes them when they are no longer needed, eliminating the need to manually call close().
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    gene_name = ""
    sequence = ""

    for line in infile:
        #Because a line read from a file typically ends with a newline character, the strip() method is used to remove the trailing newline.
        line = line.strip()

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