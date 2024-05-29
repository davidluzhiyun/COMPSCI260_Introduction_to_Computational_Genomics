from compsci260lib import *
from aligner_helpers import *


def run_local_aligner_plus():
    """Locally align O18381.fasta and P63015.fasta and report the
    optimal score and optimal local alignment information.
    """
    #
    # YOUR CODE GOES HERE
    #
    path1 = "P63015.fasta"
    title1 = "sp|P63015|PAX6_MOUSE Paired box protein Pax-6 OS=Mus musculus OX=10090 GN=Pax6 PE=1 SV=1"
    seq1 = get_fasta_dict(path1).get(title1)
    name1 = "P63015"
    path2 = "O18381.fasta"
    title2 = "sp|O18381|PAX6_DROME Paired box protein Pax-6 OS=Drosophila melanogaster OX=7227 GN=ey PE=1 SV=3"
    seq2 = get_fasta_dict(path2).get(title2)
    name2 = "O18381"

    #validate
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

    #run
    res = solve_local_aligner_plus(seq1,seq2,subst_dict,gap_penalty)
    report(res, name1, name2)


def solve_local_aligner_plus(seq1, seq2, subst_dict, gap_penalty):
    """The procedure for collecting the inputs, running the aligner,
    and returning the score and optimal alignment(s).

    Note that for each returned local alignment, starting positions
    also need to be returned. These are the positions of the first
    character in each aligned sequence relative to the original
    sequence.

    Args:
        seq1 (str): first sequence to match
        seq2 (str): second sequence to match
        subst_dict (dictionary string -> int): dictionary
            representation of the substitution matrix
        gap_penalty (int): gap penalty (penalty per gap character);
            this value should be positive because we will subtract it

    A max score may be in multiple locations, so return the optimal
    score, the locations of all the maxima, and any one optimal
    alignment as a tuple.

    Returns a tuple of:
        (the optimal alignment score as an int,

         the locations of the maxima in the dp table as a list of
         tuples. these positions will include the offset of the
         initialized penalty row and column, so that location (i,j)
         refers to the i-prefix of X and the j-prefix of Y, just as in
         lecture,

         tuple for an optimal alignment)

        The alignment will be in the form:

              (tuple of indices of the characters of the first aligned
               sequence used in the alignment),

              (tuple of indices of the characters of the second aligned
               sequence used in the alignment),

              the first aligned sequence as a string,

              the second aligned sequence as a string)

        As an example with the sequences:

            Sequence 1: TAG
            Sequence 2: TAAGATAAG

        A possible return may be:

            (11, # the optimal score

             # the two maximal locations in the dp table
             [(3, 4), (3, 9)],

             # one possible alignment:
             ((1, 3), # the nt positions mapping TA-G from TAG
              (1, 4), # the nt positions mapping TAAG from TAAGATAAG

              "TA-G", "TAAG") # the sequences of the alignment
            )

        Corresponding to two maxima with an optimal
        alignment score of 11.
    """
    #
    # YOUR CODE GOES HERE
    #

    # Initialize the DP table's data structure
    # as a list of lists of ints
    dp_table = [[0] * (len(seq2)+1) for _ in range(len(seq1)+1)]

    # Initialize the column table's data structure
    # as a list of lists of lists
    column_table = [[0] * (len(seq2)+1) for _ in range(len(seq1)+1)]

    run1 = local_aligner(seq1, seq2, subst_dict, gap_penalty, dp_table, column_table)
    op_score = run1[0]
    end_locations = run1[2]
    run2 = alignment_reconstructor(seq1, seq2, column_table, end_locations[0])
    return (op_score, end_locations, run2[0], run2[1], run2[2], run2[3])


    # example format of return tuple:
    # return (-1, [(-1, -1)], ((-1, -1), (-1, -1), "", "")

def report(result,name1,name2):
    print("Sequence 1: ", name1)
    print("Sequence 2: ", name2)
    print("Optimal Alignment Score: ", result[0])
    print("Number of Locations: ", len(result[1]))
    print("Locations")
    for l in result[1]:
        print(l[0],"in Seq1 and",l[1],"in Seq2")
    print("One optimal case:")
    print("In Seq1:")
    print(result[2][0],"-",result[2][1])
    print("In Seq2:")
    print(result[3][0], "-", result[3][1])
    print_alignment(result[4],result[5], name1=name1,name2=name2,seq1_start=result[2][0],seq2_start=result[3][0])


def local_aligner(seq1, seq2, subst_dict, gap_penalty, dp_table, column_table):
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
        column_table (list of list of ints): dynamic programming table, in the
            structure of column_table[i][j][k]. 0 represents type 3 column, 1 represents
            type 1 column, 2 represents type 2 column. -1 represents stop
            only records the bottom-most longest case

    Returns:
        (int,int,int,int): (the optimal alignment score, number of locations reaching optimal
        ,i-index of the score,j-index of the score)
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
        column_table[i][0] = -1
    for j in range(J):
        dp_table[0][j] = j * (-gap_penalty)
        column_table[0][j] = -1

    # Compute the scores for the rest of the matrix,
    # i.e. all the elements in dp_table[i][j] for i > 0 and j > 0.
    # Also records the column type in the column table
    maximum = 0
    max_count = 1
    locations = [(0, 0)]
    for i in range(1,I):
        for j in range(1,J):
            c0 = -gap_penalty + dp_table[i][j-1]
            c1 = subst_dict[seq1[i-1] + seq2[j-1]] + dp_table[i-1][j-1]
            c2 = -gap_penalty + dp_table[i-1][j]
            r = max(c0, c1, c2, 0)
            dp_table[i][j] = r
            if r == c0:
                column_table[i][j] = 0
            elif r == c1:
                column_table[i][j] = 1
            elif r == c2:
                column_table[i][j] = 2
            else:
                column_table[i][j] = -1
            if r > maximum:
                maximum = r
                max_count = 1
                locations = [(i, j)]
            elif r == maximum:
                max_count += 1
                locations.append((i,j))
    return (maximum, max_count, locations)

def alignment_reconstructor(seq1, seq2, column_table_processed, location):
    '''column_table_processed (list of list of ints): dynamic programming table,
            processed to hold only one possible column per position
        returns  alignment as tuple
    '''

    i = location[0]      # so i is m
    j = location[1]  # so j is n
    sequence1 = "-" + seq1 # prepend "-" to make the cases where I == 0 ^ J == 0 easier to deal with
    sequence2 = "-" + seq2
    r1 = ""
    r2 = ""
    while i >= 1 and j >= 1:
        if column_table_processed[i][j] == 0:
            r1 = "-" + r1
            r2 = sequence2[j] + r2
            j -= 1
            if column_table_processed[i][j] == -1:
                j += 1
                break
            continue
        if column_table_processed[i][j] == 1:
            r1 = sequence1[i] + r1
            r2 = sequence2[j] + r2
            i -= 1
            j -= 1
            if column_table_processed[i][j] == -1:
                i += 1
                j += 1
                break
            continue
        if column_table_processed[i][j] == 2:
            r1 = sequence1[i] + r1
            r2 = "-" + r2
            i -= 1
            if column_table_processed[i][j] == -1:
                i += 1
                break
            continue
    return ((i,location[0]), (j,location[1]),r1,r2)


if __name__ == "__main__":
    run_local_aligner_plus()
