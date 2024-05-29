from aligner_helpers import *
from compsci260lib import *
from GlobalAligner import *


def run_global_aligner_plus():
    """Generate the optimal global alignments between:

        2.c)
        atpa_Hs.fasta, atpaEc.fasta

        2.f)
        atpaMm.fasta, atpaHs.fasta
        atpaMm.fasta, atpaEc.fasta

        atpaBs.fasta, atpaHs.fasta
        atpaBs.fasta, atpaEc.fasta

        atpaMm.fasta, atpaBs.fasta

    For each alignment, report the optimal alignment score,
    the top-most alignment, and the bottom-most alignment.
    """

    #
    # YOUR CODE GOES HERE
    #
    path1 = "atpa_Hs.fasta"
    title1 = "sp|P25705|ATPA_HUMAN ATP synthase subunit alpha, mitochondrial OS=Homo sapiens OX=9606 GN=ATP5F1A PE=1 SV=1"
    seq1 = get_fasta_dict(path1).get(title1)
    nameh = "ATPA_HUMAN"
    path2 = "atpa_Ec.fasta"
    title2 = "sp|P0ABB0|ATPA_ECOLI ATP synthase subunit alpha OS=Escherichia coli (strain K12) OX=83333 GN=atpA PE=1 SV=1"
    seq2 = get_fasta_dict(path2).get(title2)
    namee = "ATPA_ECOLI"

    pathb = "atpa_Bs.fasta"
    titleb = "sp|P37808|ATPA_BACSU ATP synthase subunit alpha OS=Bacillus subtilis (strain 168) OX=224308 GN=atpA PE=1 SV=3"
    seqb = get_fasta_dict(pathb).get(titleb)
    nameb = "ATPA_BSUBT"
    pathm = "atpa_Mm.fasta"
    titlem = "sp|Q03265|ATPA_MOUSE ATP synthase subunit alpha, mitochondrial OS=Mus musculus OX=10090 GN=Atp5f1a PE=1 SV=1"
    seqm = get_fasta_dict(pathm).get(titlem)
    namem = "ATPA_MMUSC"

    # validation
    match = 2
    mismatch = -1
    gap_penalty = 2
    seq_type = validate_sequences(seq1, seq2)
    if seq_type == 1:
        # Both the sequences are DNA sequences so use the scores for match and
        # mismatch
        subst_matrix = create_subst_matrix_dna(match, mismatch)
    elif seq_type == 2:
        # Both the sequences are protein sequences so read in the BLOSUM62
        # substitution matrix
        subst_matrix = create_subst_matrix_aa("BLOSUM62.txt")
        gap_penalty = 8
    else:
        sys.exit("Input sequences are of different types: not both DNA or both protein")

    subst_dict = create_subst_matrix_dict(subst_matrix)

    result = solve_global_aligner_plus(seq1, seq2,subst_dict,gap_penalty)

    report(result, nameh, namee)

    result1 = solve_global_aligner_plus(seqm, seq1, subst_dict, gap_penalty)
    report(result1, namem, nameh)

    result2 = solve_global_aligner_plus(seqb, seq1, subst_dict, gap_penalty)
    report(result2, nameb, nameh)

    result3 = solve_global_aligner_plus(seqm, seq2, subst_dict, gap_penalty)
    report(result3, namem, namee)

    result4 = solve_global_aligner_plus(seqb, seq2, subst_dict, gap_penalty)
    report(result4, nameb, namee)

    result5 = solve_global_aligner_plus(seqm, seqb, subst_dict, gap_penalty)
    report(result5, namem, nameb)

def report(result,name1,name2):
    print("Sequence 1: ", name1)
    print("Sequence 2: ", name2)
    print("Optimal Alignment Score: ", result[0])
    print()
    print("Top-most:")
    print()
    print_alignment(result[1][0],result[1][1],name1=name1,name2=name2)
    print("Bottom-most:")
    print()
    print_alignment(result[2][0],result[2][1],name1=name1,name2=name2)

def solve_global_aligner_plus(seq1, seq2, subst_dict, gap_penalty):
    """The overall procedure for collecting the inputs, running the aligner,
    filling in the DP table, and returning the final value and alignments.

    Args:
        seq1 (str): first sequence to be aligned
        seq2 (str): second sequence to be aligned
        subst_dict (dictionary string -> int): dictionary representation of the
            substitution matrix
        gap_penalty (int): gap penalty (penalty per gap character); this
            value should be positive because we will subtract it

    Returns a tuple of:
        (the optimal alignment score as an int,
         the top-most alignment achieving this score as a tuple of strings,
         the bottom-most alignment achieving this score as a tuple of strings)

        Example output:

            (6, ("AT-AGG", "ATCCGG"), ("ATA-GG", "ATCCGG"))

    Note: If you do the extra challenge to report all optimal alignments,
    you can lengthen the size of the return tuple, but ensure that its second
    element (i.e., the first alignment) remains the top-most alignment, while
    the last element is the bottom-most alignment. e.g.

        (optimal score, (top-most alignment sequences), ...,
         (bottom-most alignment sequences))
    """

    #
    # YOUR CODE GOES HERE
    #


    # Initialize the DP table's data structure
    # as a list of lists of ints
    dp_table = [[0] * (len(seq2)+1) for _ in range(len(seq1)+1)]

    # Initialize the column table's data structure
    # as a list of lists of lists
    column_table = [[[] for j in range(len(seq2)+1)] for i in range(len(seq1)+1)]

    # call global aligner
    max_value = global_aligner_plus(seq1, seq2, subst_dict, gap_penalty, dp_table, column_table)

    # process column table
    column_table_top = [[max(column_table[i][j]) for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]
    column_table_bottom = [[min(column_table[i][j]) for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]
    top_most = alignment_reconstructor(seq1,seq2,column_table_top)
    bottom_most = alignment_reconstructor(seq1,seq2,column_table_bottom)

    return (max_value, top_most, bottom_most)

def global_aligner_plus(seq1, seq2, subst_dict, gap_penalty, dp_table, column_table):
    """A dynamic programming algorithm that takes two sequences and returns the
    score of the optimal alignment while updating the column_table.

    Args:
        seq1 (str): first sequence to be aligned
        seq2 (str): second sequence to be aligned
        subst_dict (dict): substitution matrix stored as a dictionary, with
            keys that reference the two characters being aligned, and values
            being the corresponding score.  See the create_subst_matrix_dict()
            function to know how this works.

        gap_penalty (int): linear gap penalty (penalty per gap character); this
            value should be positive because we will subtract it

        dp_table (list of list of ints): dynamic programming table, in the
            structure of dp_table[i][j]
        column_table (list of list of of list ints): dynamic programming table, in the
            structure of column_table[i][j][k]. 0 represents type 3 column, 1 represents
            type 1 column, 2 represents type 2 column.

    Returns:
        (int): the optimal alignment score
    """

    # the dp table has len(seq1) + 1 rows and len(seq2) + 1 columns
    I = len(dp_table)      # so I is 1 more than m
    J = len(dp_table[0])   # so J is 1 more than n

    # Initialize the dp table with solutions to base cases using linear gap
    # penalty
    # also initializes the columntable
    # column_table [0][0] is initialized to [2] to prevent error with max
    for i in range(I):
        dp_table[i][0] = i * (-gap_penalty)
        column_table[i][0].append(2)
    for j in range(J):
        dp_table[0][j] = j * (-gap_penalty)
        column_table[0][j].append(2)

    # Compute the scores for the rest of the matrix,
    # i.e. all the elements in dp_table[i][j] for i > 0 and j > 0.
    # Also records the column type in the column table
    for i in range(1,I):
        for j in range(1,J):
            c0 = -gap_penalty + dp_table[i][j-1]
            c1 = subst_dict[seq1[i-1] + seq2[j-1]] + dp_table[i-1][j-1]
            c2 = -gap_penalty + dp_table[i-1][j]
            r = max(c0, c1, c2)
            dp_table[i][j] = r
            if r == c0:
                column_table[i][j].append(0)
            if r == c1:
                column_table[i][j].append(1)
            if r == c2:
                column_table[i][j].append(2)
    # The optimal score is found at the lower right corner of the dp table:
    return dp_table[I-1][J-1]

def alignment_reconstructor(seq1, seq2, column_table_processed):
    '''column_table_processed (list of list of ints): dynamic programming table,
            processed to hold only one possible column per position
        returns  alignment as tuple
    '''

    i = len(column_table_processed) - 1      # so i is m
    j = len(column_table_processed[0]) - 1  # so j is n
    sequence1 = "-" + seq1 # prepend "-" to make the cases where I == 0 ^ J == 0 easier to deal with
    sequence2 = "-" + seq2
    r1 = ""
    r2 = ""
    while i > 0 or j > 0:
        if column_table_processed[i][j] == 0:
            r1 = "-" + r1
            r2 = sequence2[j] + r2
            j -= 1
            continue
        if column_table_processed[i][j] == 1:
            r1 = sequence1[i] + r1
            r2 = sequence2[j] + r2
            i -= 1
            j -= 1
            continue
        if column_table_processed[i][j] == 2:
            r1 = sequence1[i] + r1
            r2 = "-" + r2
            i -= 1
            continue
    return (r1,r2)




if __name__ == "__main__":
    run_global_aligner_plus()
