import re

from compsci260lib import get_fasta_dict


def run_orfs():
    """Report the number of ORFs if the minimum ORF length is 10 amino acids,
    40 amino acids, or 60 amino acids.  Also report the average length (in
    amino acids) of the identified ORFs for the three cases.
    """

    #
    # Your code goes here
    #

    # get the string
    sars_cov2_wu_fasta_path = "sars_cov2_wu.fasta"
    sars_cov2_wu_genomic = get_fasta_dict(sars_cov2_wu_fasta_path)["MN908947.3"]

    # processing
    lengths = [10, 40, 60]
    for length in lengths:
        my_orfs = find_orfs(sars_cov2_wu_genomic, length)
        my_res = summarize_orfs(my_orfs)
        print("If the minimum ORF length is {} amino acids, there are {} ORF(s) with average length {} in amino acids".format(length, my_res[0], my_res[1]))
    return  # placeholder code, for a valid function


def summarize_orfs(orfs):
    """Summarize ORFs identified from the find_orfs procedure as a count of the
    number of found orfs and the average length of the found ORFs (in amino
    acids)

    Args:
        orfs (list): a list of dictionaries of found ORFs

    Returns:
        tuple: (The number of ORFs found (int), Average ORF length (float))
    """

    #
    # Your code here
    #
    num_f = len(orfs)
    if num_f == 0:
        avg = 0
    else:
        ls = [d["aalength"] for d in orfs]
        avg = sum(ls)/len(ls)

    return (num_f, avg)  # replace with the tuple described above


def find_orfs(seq, min_length_aa=0):
    """This is a function for finding sufficiently long ORFs in all reading
    frames in a sequence of DNA or RNA.  By default, the sequence is assumed
    to be single-stranded.

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
        frame (int): The nucleotide offset in which the ORF was found. (Must be
        0, 1, or 2)
        stop (int): the nucleotide position of the end of the ORF
        start (int): the nucleotide position of the start of the ORF
        stopcodon (str): the nucleotide triplet of the stop codon
        nlength (int): the length (in nucleotides) of the ORF
        strand (str): the strand of the found ORF (Must be "W" or "C")

    A valid return list may look something like this:
    [
        {
            "frame": 0,
            "stop": 13413,
            "aalength": 4382,
            "start": 265,
            "stopcodon": "UAA",
            "nlength": 13149,
            "strand": "W"
        },
        {
            "frame": 0,
            "stop": 27063,
            "aalength": 221,
            "start": 26398,
            "stopcodon": "UAA",
            "nlength": 666,
            "strand": "C"
        }
    ]
    """

    #
    # Your code here
    #

    # Inspired by the greedy behavior described in https://docs.python.org/3/library/re.html
    # Regular expression similar to that used in cloning.py
    #RNA
    re_start = "aug"
    re_mid = "((?!((uag)|(uaa)|(uga)))([aucg]{3}))"
    re_end = "((uag)|(uaa)|(uga))"


    #DNA
    re_start1 = "(atg)"
    re_mid1 = "((?!((tag)|(taa)|(tga)))([atcg]{3}))"
    re_end1 = "((tag)|(taa)|(tga))"

    #

    # calculate the repetition
    rep = max(min_length_aa - 1, 0)
    # resulting re
    re_rep = "{" + str(rep) + ",}"
    regex = re_start + re_mid + re_rep + re_end
    regex1 = re_start1 + re_mid1 + re_rep +re_end1
    # search
    prog = re.compile(regex)
    prog1 = re.compile(regex1)
    it = prog.finditer(seq)
    it1 = prog1.finditer(seq)
    ls = []
    for mat in list(it) + list(it1):
        my_start = mat.start() + 1
        my_stop = mat.end()
        my_stop_codon = seq[mat.end() - 3:mat.end()].upper()
        my_nlength = mat.end() - mat.start()
        my_aalength = my_nlength//3 - 1
        my_frame = mat.start() % 3
        my_strand = "W"
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
    """Run run_orfs(). Do not modify this code"""
    run_orfs()
