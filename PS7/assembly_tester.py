from compsci260lib import *


def run_assembly_tester():
    """Read in the read and contig files, verify the reads in each contig, and estimate
    the gap length between the contigs.
    """
    reads_file = "paired.reads.fasta"
    contigs_file = "contigs.fasta"

    # Load the two fasta files
    reads = get_fasta_dict(reads_file)
    contigs = get_fasta_dict(contigs_file)

    # Determine how the reads map to the contigs
    contig_reads = find_contig_reads(reads, contigs)

    # Report:
    #   - Any reads that are not consistent with the overall assembly based
    #     on the checks done by find_contig_reads()
    #   - The read pairs where both reads match to (distinct) contigs in supercontig1,
    #   and their estimated gap lengths
    #
    # YOUR CODE HERE
    #
    counts = [0, 0, 0]
    seqs = ["", "", ""]
    spanning = []

    for key in list(contig_reads.keys()):
        # neither reads are present
        if contig_reads[key]["contig_a"] is None and contig_reads[key]["contig_b"] is None:
            counts[0] += 1
            seqs[0] = seqs[0] + key + "\n"
        # at least one of the pair is in some contig, we can't find both reads in one contig
        elif contig_reads[key]["contig_a"] != contig_reads[key]["contig_b"]:
            counts[1] += 1
            seqs[1] = seqs[1] + key + "\n"
            # count the spanning sequences for d and forward
            if contig_reads[key]["contig_a"] is not None and contig_reads[key]["contig_b"] is not None:
                spanning.append(key)
        else:
            # distance from the beginning of the first read to the end of the second read
            # assume distance is inclusive
            dist = max(abs(contig_reads[key]["start_a"] - contig_reads[key]["end_b"]),
                       abs(abs(contig_reads[key]["start_b"] - contig_reads[key]["end_a"]))) + 1
            # both reads in one contig, but the length is off
            if abs(dist - 2000) > 10:
                counts[2] += 1
                print(key)
    print("{} pair(s) have neither read found in contigs, therefore from another project:".format(counts[0]))
    print(seqs[0])
    print("{} pair(s) have at least one read in some contig, but we can't find both reads in the same contig:".format(counts[1]))
    print(seqs[1])
    print("{} pair(s) have both reads in the same contig, but the outer distance (inclusive) isn't 2000+-10:".format(counts[2]))
    print(seqs[2])
    print("{} viable pair(s)".format(len(contig_reads) - sum(counts)))
    print()

    # look for super contig
    myset = set()
    spanning1 = []
    for key in spanning:
        # use set to remove duplicate
        myset.add((contig_reads[key]["contig_a"], contig_reads[key]["contig_b"]))
        # spanning pairs in
        if contig_reads[key]["contig_a"] == "contig1" or contig_reads[key]["contig_b"] == "contig1":
            spanning1.append(key)
    print("{} supercontigs:".format(len(myset)))
    for entry in myset:
        print(entry[0] + ", " + entry[1])

    print()
    # now that we know that supercontig1 is contig1,contig3
    print("{:<11} {:<16} {:<13} {:<11}".format("Read name", "Gap size range", "Lower bound", "Upper bound"))
    print("-"*54)
    for key in spanning1:
        # length that overlap with contig1
        left = len(contigs["contig1"]) - contig_reads[key]["start_a"] + 1
        # length that overlap with contig3
        right = contig_reads[key]["end_b"]
        gap = 2000 - left -right
        # wiggle room comes from the uncertainty in the length of the fragment
        upper = gap + 10
        lower = gap -10
        range = str(gap) + "+-10"
        print("{:<11} {:<16} {:<13} {:<11}".format(key, range, lower, upper))

def find_contig_reads(reads, contigs):
    """
    Determine the contig in which each sequencing read appears (if any), along with
    where in the contig it matches.  The `contigs` dict will have a collection of 
    contig names mapped to contig sequences.  The `reads` dict contains separate keys 
    (labeled 'a' and 'b') for the two reads in each read pair.  However, this function
    returns a dictionary with a single key for each read pair (i.e., without 'a' or 'b').

    The value for each read-pair key will itself be a dictionary with the following keys:

        - 'contig_a' (str): the contig in which read 'a' was found, as 
          <contig name> or None (<contig name> will be a key in `contigs` dict)
        - 'start_a' (int): the start position (1-indexed) read 'a' mapped to
          within its respective contig (None if not found in any contig)
        - 'end_a' (int): the end position (1-indexed) read 'a' mapped to
          within its respective contig (None if not found in any contig)
        - 'contig_b' (str): the contig in which read 'b' was found, as
          <contig name> or None. (see 'contig_a' for example).
        - 'start_b' (int): the start position (1-indexed) read 'b' mapped to
          within its respective contig (None if not found in any contig)
        - 'end_b' (int): the end position (1-indexed) read 'b' mapped to
          within its respective contig (None if not found in any contig)

    The returned dictionary should look something like:
    {
        'seq1': {
            'contig_a': 'contig1',
            'start_a': 301,
            'end_a': 800,
            'contig_b': None
            'start_b': None,
            'end_b': None,
        },
        'seq2': {
            'contig_a': 'contig2',
            'start_a': 1101,
            'end_a': 1600,
            'contig_b': 'contig1'
            'start_b': 201,
            'end_b': 700,
        },
        'seq3' : {
            'contig_a': None,
            'start_a': None,
            'end_a': None,
            'contig_b': None
            'start_b': None,
            'end_b': None,
        },
        ...
    }

    Arguments:
        reads (dict str to str): dictionary of reads, mapping read names to sequences
        contigs (dict str to str): dictionary of contigs, mapping contig names to sequences

    Returns:
        Dictionary mapping read-pairs to information about their reads' locations in contigs.
    """

    #
    # YOUR CODE HERE
    #
    result = {}
    for i in range(1, int(len(reads) / 2) + 1):
        # default to none
        my_dict = {
            'contig_a': None,
            'start_a': None,
            'end_a': None,
            'contig_b': None,
            'start_b': None,
            'end_b': None,
        }
        for part in ("a", "b"):
            my_seq = reads["seq" + str(i) + part]
            for key in list(contigs.keys()):
                # using string.find to perform matching in all contigs
                start = contigs[key].find(my_seq)
                if start < 0:
                    # if not found, do nothing
                    continue
                else:
                    # if found, update entry and stop searching
                    my_dict["contig_" + part] = key
                    # index converted to nucleotides (inclusive)
                    my_dict["start_" + part] = start + 1
                    my_dict["end_" + part] = start + len(my_seq)
                    break
        result["seq" + str(i)] = my_dict
    return result


if __name__ == '__main__':
    """Call run_assembly_tester(). Do not modify this block."""
    run_assembly_tester()
