import re

from compsci260lib import get_fasta_dict, reverse_complement, translate


def run_plasmid():
    """Function to
    1) Run the simple_assembler function to assemble the plasmid from a .fasta of reads
    2) Run the find_orfs_circular_double_stranded function to find ORFs in the assembled
       circular plasmid (considering both Watson and Crick strands)
    3) Report the number of ORFs found that are of >= 50 amino acids long, coding fractions
    4) Translate the longest ORF to its amino acid sequence and print it out.
    """
    # Load the plasmid reads from fasta, and ensure they are in proper order to be assembled
    #
    # Your code here
    #
    # reads .fasta and convert to list
    plasmid_path = "plasmid.fasta"
    reads_d = get_fasta_dict(plasmid_path)
    reads = []
    reads.append(reads_d.pop("start"))
    for key in list(reads_d):
        reads.append(reads_d[key])

    # Assemble the reads into a single-stranded linearized version of the plasmid:
    plasmid_dna = simple_assembler(reads)

    # Report the length of the assembled plasmid
    #
    # Your code here
    #
    print("Length of assembled plasmid: {}".format(len(plasmid_dna)))
    i = 0
    while i + 100 < len(plasmid_dna):
        print(plasmid_dna[i:i + 100])
        i += 100
    print(plasmid_dna[i:])
    # Search for ORFs in the reconstructed plasmid DNA and report your results
    #
    # Your code here
    #
    orfs = find_orfs_circular_double_stranded(plasmid_dna, 50)
    print("\nORFs in the plasmid (Start and stop in nucleotides and inclusive):\n")
    for orf in orfs:
        print("    Frame:", orf["frame"])
        print("    Stop:", orf["stop"])
        print("    Length in amino acids", orf["aalength"])
        print("    Start:", orf["start"])
        print("    Stop Codon:", orf["stopcodon"])
        print("    Length in nucleotides:", orf["nlength"])
        print("    Strand:", orf["strand"])
        print()
    print("    {} ORF(s) in Total".format(len(orfs)))
    '''
    for orf in orfs:
        if orf["strand"] == "W":
            print("{}-{} {}".format(orf["start"], orf["stop"] - 3, orf["nlength"] - 3))
        else:
            print("{}-{} {}".format(len(plasmid_dna)+1-orf["stop"] + 3, len(plasmid_dna)+1-orf["start"], orf["nlength"] - 3))
    '''
    # Find the longest ORF and translate
    #
    # Your code here
    #
    longest = orfs[0]
    for orf in orfs:
        if orf["nlength"] > longest["nlength"]:
            longest = orf
    start_index = longest["start"] - 1
    if longest["start"] > longest["stop"]:
        stop_index = longest["stop"] + len(plasmid_dna)
    else:
        stop_index = longest["stop"]
    if longest["strand"] == "C":
        seq = orf_help2_flip(plasmid_dna)[start_index:stop_index]
    else:
        seq = plasmid_dna[start_index:stop_index]
    prt = translate(seq)
    print(prt)


def simple_assembler(reads):
    """Given a list of reads, as described in the problem, return an assembled
    DNA sequence, as a string. For consistency, use the first entry in the
    fragment reads list as the starting position of the returned sequence.

    For example, if we were to take in a list of three reads, 31 nucleotides
    long each. The last 15 nucleotides of each read would overlap with one
    other read, and the assembled sequence would be 48 nucleotides long with
    the sequence starting with the beginning of the first read.

    Args:
        my_reads (list): list of sequence strings as reads

    Returns:
         str: an assembled genomic sequence as a string starting with the first
              read in `reads`
    """

    #
    # Your code here
    #
    my_reads = reads.copy()
    for i in range(len(my_reads) - 2):
        for j in range(i + 1, len(my_reads)):
            str1 = my_reads[i]
            str2 = my_reads[j]
            if str1[len(str1) - 15:] == str2[0:15]:
                str = str2
                my_reads[j] = my_reads[i + 1]
                my_reads[i + 1] = str

    r = ""
    for s in my_reads:
        r = r + s[:len(s) - 15]

    return r


def find_orfs_circular_double_stranded(seq, min_length_aa=0):
    """This is a function for finding sufficiently long ORFs in all reading
    frames in a sequence of double-stranded circular DNA.

    The function takes as input parameters: a string representing a genomic
    sequence, the minimum length (in amino acids) for an ORF before it will be
    returned (which defaults to 0).

    Args:
        seq (str): a genomic sequence
        min_length_aa (int): minimum length of found ORFs in amino acids

    Returns:
        list: of dictionaries with information on each ORF found.

    Where each ORF found is represented by a dictionary with
    the following keys:
        frame (int): the reading frame (or nucleotide offset) in which
            the ORF was found (must be 0, 1, or 2)
        start (int): the nucleotide position of the start of the ORF
            (relative to 5' end of the found ORF's strand)
        stop (int): the nucleotide position of the end of the ORF
            (relative to 5' end of the found ORF's strand)
        stopcodon (str): the nucleotide triplet of the stop codon
        nlength (int): the length (in nucleotides) of the ORF
        aalength (int): the length (in amino acids) of the translated protein
        strand (str): the strand of the found ORF (must be "W" or "C")

    A valid return list may look something like this:
    [
        {
            "frame": 0,
            "stop": 13413,
            "aalength": 4382,
            "start": 265,
            "stopcodon": "TAA",
            "nlength": 13149,
            "strand": "W"
        },
        {
            "frame": 0,
            "stop": 27063,
            "aalength": 221,
            "start": 26398,
            "stopcodon": "TAG",
            "nlength": 666,
            "strand": "C"
        }
    ]
    """

    #
    # Your code here
    #
    l1 = orf_help1_match(seq + seq, min_length_aa)
    l1 = orf_help3_process(l1, len(seq))

    flip_seq = orf_help2_flip(seq)

    l2 = orf_help1_match(flip_seq + flip_seq, min_length_aa, "C")
    l2 = orf_help3_process(l2, len(seq))
    return l1 + l2


# Compare the two list, remove duplicates and change coordinate
def orf_help3_process(list1, length):
    # remove duplicated results
    my_list = [orf for orf in list1 if orf["start"] < length]

    tracker = [False for i in range(len(my_list))]
    ret_list = []
    for orf in my_list:
        if orf["stop"] > length:
            orf["stop"] = orf["stop"] - length
    # remove overlap
    for i in range(len(my_list)):
        if tracker[i]:
            continue
        tracker[i] = True
        longest = my_list[i]
        for j in range(i + 1, len(my_list)):
            if tracker[j]:
                continue
            if my_list[j]["stop"] == longest["stop"]:
                tracker[j] = True
                if my_list[j]["nlength"] >= longest["nlength"]:
                    longest = my_list[j]
        ret_list.append(longest)
    return ret_list



# Finds the complement strand
def orf_help2_flip(seq):
    assert isinstance(seq, str)
    ret_seq = ""
    cpl = { "a": "t",
            "t": "a",
            "c": "g",
            "g": "c"}
    for i in range(len(seq) - 1, -1, -1):
        ret_seq = ret_seq + cpl[seq[i]]
    return ret_seq

# Check all orf for a straight strand
def orf_help1_match(seq,min_length_aa, strand="W"):

    # Inspired by https://stackoverflow.com/questions/43149086/python-3-regex-find-all-overlapping-matches-start-and-end-index-in-a-string
    # DNA
    re_start1 = "(atg)"
    re_mid1 = "((?!((tag)|(taa)|(tga)))([atcg]{3}))"
    re_end1 = "((tag)|(taa)|(tga))"


    # calculate the repetition
    rep = max(min_length_aa - 1, 0)
    # resulting re
    re_rep = "{" + str(rep) + ",}"
    regex1 = "(?=(" + re_start1 + re_mid1 + re_rep + re_end1 + "))"
    # search
    prog1 = re.compile(regex1)
    it1 = prog1.finditer(seq)
    ls = []
    for mat in list(it1):
        my_start = mat.start(1) + 1
        my_stop = mat.end(1)
        my_stop_codon = seq[mat.end(1) - 3:mat.end(1)].upper()
        my_nlength = mat.end(1) - mat.start(1)
        my_aalength = my_nlength // 3 - 1
        my_frame = mat.start(1) % 3
        my_strand = strand
        ls.append({
            "frame": my_frame,
            "stop": my_stop,
            "aalength": my_aalength,
            "start": my_start,
            "stopcodon": my_stop_codon,
            "nlength": my_nlength,
            "strand": my_strand
        })

    return ls


if __name__ == "__main__":
    run_plasmid()
