import math

from compsci260lib import *
from aligner_helpers import *


def run_ag_aligner_plus():
    """Align atpa_Hs.fasta and atpaEc.fasta and report the optimal
    alignment score, the top-most alignment, and the bottom-most
    alignment.
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

    # parameters
    gap_penalty = 1
    affine_penalty = 11

    assert validate_sequences(seq1, seq2) == 2
    subst_matrix = create_subst_matrix_aa("BLOSUM62.txt")
    subst_dict = create_subst_matrix_dict(subst_matrix)

    result = solve_ag_aligner_plus(seq1, seq2, subst_dict, gap_penalty, affine_penalty)
    report(result, nameh, namee)

# Helper function for reporting
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


def solve_ag_aligner_plus(seq1, seq2, subst_dict, gap_penalty, affine_penalty):
    """The procedure for collecting the inputs, running the aligner,
    and returning the score and optimal alignments.

    Args:
        seq1 (str): first sequence to match
        seq2 (str): second sequence to match
        subst_dict (dictionary string -> int): dictionary
            representation of the substitution matrix
        gap_penalty (int): gap penalty (penalty per gap character);
            this value should be positive because we will subtract it
        affine_penalty (int): affine penalty; as a positive integer

    Returns a tuple of:
        (the optimal alignment score as an int,
         the top-most alignment achieving this score as a tuple of
         strings, the bottom-most alignment achieving this score as a
         tuple of strings)

        Example output:
            (6, ("AT-AGG", "ATCCGG"), ("ATA-GG", "ATCCGG"))
    """

    #
    # YOUR CODE GOES HERE
    #

    # Initialize the DP table's data structure
    # as a list of lists of list  of ints
    dp_table = [[[0, 0, 0] for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    # Initialize the trace table's data structure
    # as a list of lists of lists of lists
    trace_table = [[[[], [], []] for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    # run global aligner
    run = global_aligner_affine_plus(seq1, seq2, subst_dict, gap_penalty, affine_penalty, dp_table, trace_table)
    max_value = run[0]

    # process column table and entrance
    entrance_top = max(run[1:])
    entrance_bottom = min(run[1:])
    column_table_top = [[[max(trace_table[i][j][k]) for k in range(3)] for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]
    column_table_bottom = [[[min(trace_table[i][j][k]) for k in range(3)] for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    # trace
    top_most = alignment_reconstructor_affine(seq1, seq2, column_table_top, entrance_top)
    bottom_most = alignment_reconstructor_affine(seq1, seq2, column_table_bottom, entrance_bottom)

    # return -1, ("", ""), ("", "")
    return (max_value, top_most, bottom_most)

def global_aligner_affine_plus(seq1, seq2, subst_dict, gap_penalty, affine_penalty, dp_table, trace_table):
    """A dynamic programming algorithm that takes two sequences and returns the
    score of the optimal alignment while updating the layer_table.

    Args:
        seq1 (str): first sequence to be aligned vg
        seq2 (str): second sequence to be aligned
        subst_dict (dict): substitution matrix stored as a dictionary, with
            keys that reference the two characters being aligned, and values
            being the corresponding score.  See the create_subst_matrix_dict()
            function to know how this works.

        gap_penalty (int): linear gap penalty (penalty per gap character); this
            value should be positive because we will subtract it
        affine_penalty: affine gap penalty (penalty per gap); this value should
        be positive because we will subtract it
        dp_table (list of list of list of ints): dynamic programming table, in the
            structure of dp_table[i][j][k] k = 0 represents F, 1 represents
            D, 2 represents E.
        trace_table (list of list of of list of list of ints): dynamic programming table, in the
            structure of column_table[i][j][k][h]. Record the layer to jump to

    Returns:
        (int,int): the optimal alignment score, starting layer for trace
    """
    I = len(dp_table)  # so I is 1 more than m
    J = len(dp_table[0])  # so J is 1 more than n

    # Initialize the dp table
    # penalty
    # also initializes the columntable
    # meaningless cells in trace_table are also initialized to prevent error with max and min
    dp_table[0][0][0] = - math.inf
    dp_table[0][0][1] = 0
    dp_table[0][0][2] = - math.inf
    # meaningless, just to stop min and max from throwing error
    trace_table[0][0] = [[1], [1], [1]]
    for i in range(1, I):
        dp_table[i][0][0] = - math.inf
        dp_table[i][0][1] = - math.inf
        dp_table[i][0][2] = -affine_penalty - i * (gap_penalty)
        trace_table[i][0] = [[2], [2], [2]]
        '''
        # technically wrong when i = 1, but enough for tracing
        trace_table[i][0][0].append(2)
        # meaningless, just to feed min and max
        trace_table[i][0][1].append(2)
        trace_table[i][0][2].append(2)
        '''
    for j in range(1, J):
        dp_table[0][j][0] = -affine_penalty - j * (gap_penalty)
        dp_table[0][j][1] = - math.inf
        dp_table[0][j][2] = - math.inf
        trace_table[0][j] = [[0], [0], [0]]

    # Compute the scores for the rest of the matrix,
    # Also fills the trace table
    for i in range(1, I):
        for j in range(1, J):
            # F
            res0 = max_is(dp_table[i][j - 1][0] - gap_penalty,
                          dp_table[i][j - 1][1] - gap_penalty - affine_penalty,
                          dp_table[i][j - 1][2] - gap_penalty - affine_penalty)
            dp_table[i][j][0] = res0[0]
            trace_table[i][j][0] = res0[1:]
            # D
            res1 = max_is(dp_table[i - 1][j - 1][0],
                          dp_table[i - 1][j - 1][1],
                          dp_table[i - 1][j - 1][2])
            dp_table[i][j][1] = res1[0] + subst_dict[seq1[i-1] + seq2[j-1]]
            trace_table[i][j][1] = res1[1:]
            # E
            res2 = max_is(dp_table[i - 1][j][0] - gap_penalty - affine_penalty,
                          dp_table[i - 1][j][1] - gap_penalty - affine_penalty,
                          dp_table[i - 1][j][2] - gap_penalty)
            dp_table[i][j][2] = res2[0]
            trace_table[i][j][2] = res2[1:]

    # The optimal score is found at the lower right corner of the dp table:
    return max_is(dp_table[I - 1][J - 1][0], dp_table[I - 1][J - 1][1], dp_table[I - 1][J - 1][2])


def alignment_reconstructor_affine(seq1, seq2, trace_table_processed, entrance):
    '''column_table_processed (list of list of ints): dynamic programming table,
            processed to hold only one possible column per position
        returns  alignment as tuple
    '''
    i = len(trace_table_processed) - 1      # so i is m
    j = len(trace_table_processed[0]) - 1  # so j is n
    sequence1 = "-" + seq1 # prepend "-" to make the cases where I == 0 ^ J == 0 easier to deal with
    sequence2 = "-" + seq2
    r1 = ""
    r2 = ""
    my_layer = entrance
    while i > 0 or j > 0:
        if my_layer == 0:
            r1 = "-" + r1
            r2 = sequence2[j] + r2
            my_layer = trace_table_processed[i][j][my_layer]
            j -= 1
        elif my_layer == 1:
            r1 = sequence1[i] + r1
            r2 = sequence2[j] + r2
            my_layer = trace_table_processed[i][j][my_layer]
            i -= 1
            j -= 1
        else:
            r1 = sequence1[i] + r1
            r2 = "-" + r2
            my_layer = trace_table_processed[i][j][my_layer]
            i -= 1
    return (r1, r2)


# auxiliary function for returning the max of three terms and the indices of the max
def max_is(t0, t1, t2):
    m = max(t0, t1, t2)
    l = [m]
    if m == t0:
        l.append(0)
    if m == t1:
        l.append(1)
    if m == t2:
        l.append(2)
    return l


if __name__ == "__main__":
    run_ag_aligner_plus()
