from compsci260lib import *
from UltrametricAdditive import is_ultrametric, is_additive


def build_tree():
    """
    Read the aligned student sequences, compute the dictionary of distances,
    construct the appropriate phylogenetic tree.
    """

    # Load the aligned student sequences and create the dictionary of distances
    # in the same format as found in UltrametricAdditive.py. You will need to
    # convert the student names to integers ("Student_1" -> 1)
    #
    # YOUR CODE HERE
    #
    dist = {}
    # Uncomment the following line to print out the distance dictionary
    # print_dist(dist)
    students = get_fasta_dict("students.aligned.fasta")
    n = 7
    for i in range(1, n):
        for j in range(i + 1, n+1):
            key = str(i) + "," + str(j)
            prefix = "Student_"
            value = compute_dist(students[prefix + str(i)], students[prefix + str(j)])
            dist[key] = value
    print_dist(dist)

    # Check if the distances are ultrametric
    threshold = 0.005  # problem-specific distance threshold for this problem
    if is_ultrametric(dist, threshold=threshold):
        print("\nThe distance is ultrametric.")
    else:
        print("\nThe distance is not ultrametric.")

    # Check if the distances are additive
    if is_additive(dist, threshold=threshold):
        print("\nThe distance is additive.\n")
    else:
        print("\nThe distance is not additive.\n")

    # Report the Newick representation of the phylogenetic tree    
    #
    # YOUR CODE HERE
    #
    seq_names = [i + 1 for i in range(n)]
    print("Newick representation of the phylogenetic tree:")
    print(compute_nj_newick(seq_names,dist))
    print()

    # Call `summarize_alignment` to report the differences between the two
    # most similar and two most different sequence alignments
    #
    # YOUR CODE HERE
    #
    title1 = "Two SARS-CoV-2 genome sequences that are most similar:"
    title2 = "Two SARS-CoV-2 genome sequences that are most different:"
    title3 = "Two genome sequences that are most different overall:"
    report_alignment(1, 6, title1)
    report_alignment(3, 7, title2)
    report_alignment(2, 5, title3)


# helper function for
def report_alignment(num1, num2, title):
    students = get_fasta_dict("students.aligned.fasta")
    prefix = "Student_"
    print(title)
    print("Student {} and Student {}".format(num1, num2))
    match, mismatch, gap = summarize_alignment(students[prefix + str(num1)], students[prefix + str(num2)])
    print("Match(es):", match)
    print("Mismatch(es):", mismatch)
    print("Gap(s):", gap)
    print()


def compute_nj_newick(seq_names, dist):
    """
    Performs Neighbor Joining to construct the phylogenetic tree from a
    distance table.

    Args:
        seq_names (list of ints): representing the sequence names.
                e.g. [1, 2, ..] for ["Student_1", "Student_2", ...]

        dist (dict of str to float): distance table mapping pairs of students 
            to float distances. Refer to UltrametricAdditive.py for examples of
            distance tables.

    Returns:
        the Newick representation of the phylogenetic tree as a string
    """

    # ------------- Implementation of the Neighbor Joining algorithm ----------
    # Keeping track of variable names:

    # dist              - dictionary containing the computed pair-wise
    #                     distances between nodes
    # node_list         - array containing the list of current nodes (L), which
    #                     gradually decreases in size while iterating to build 
    #                     the tree
    # avg_dist          - dictionary containing the averaged distances 
    #                     (r values) for all of the current nodes (those in L)
    # D                 - dictionary containing the "adjusted" pairwise
    #                     distances between nodes
    # newick            - dictionary to maintain the Newick representation of
    #                     each leaf node or subtree

    # ------------- Initialization: -------------------------------------------

    node_list = seq_names  # L = the list of current nodes
    newick = {}
    for i in range(1, len(node_list)+1):
        newick[i] = "" + str(i)

    avg_dist = {}  # to hold the averaged distances (r values) for all current nodes

    for i in range(1, len(node_list) + 1):
        
        avg_dist[i] = 0       
        for j in range(1, len(node_list) + 1):
            
            if i != j:
                avg_dist[i] += dist["%d,%d" % (i,j)] if i<j else \
                               dist["%d,%d" % (j,i)]
        
        avg_dist[i] = avg_dist[i] / (len(node_list) - 2)

    max_node = len(node_list)  # the maximum key used for a node
    
    # -------------- Iteration to build the tree --------------------

    # As long as the list contains more than 2 nodes, iterate 
    while len(node_list) > 2:
        
        # ---------- Begin your code -------------
   
        # Compute the "adjusted" distances between nodes using the original
        # distances (from dist) and averaged distances (from avg_dist)

        # Let D be the dict to contain "adjusted" distances
        D = {}

        # Loop through each pair of nodes as entered in the dist dict
        # Use the entries from the avg_dist dict and calculate entries
        # for the D dict
        for i in range(len(node_list)-1):
            for j in range(i + 1, len(node_list)):
                D["%d,%d" % (node_list[i], node_list[j])] = dist["%d,%d" % (node_list[i], node_list[j])] \
                                                            - avg_dist[node_list[i]] - avg_dist[node_list[j]]

        # Pick the pair i,j in node_list for which adjusted distance D_ij is
        # minimal.
        # You may find the function two_min_in_dict helpful.
        (i,j) = two_min_in_dict(D)  # Replace with your pair

        # Define a new node m and set dist[k,m] for all nodes k in node_list
        # as (dist[i,k] + dist[j,k] - dist[i,j]) / 2

        # max_node had been earlier set to the largest key used for a node
        m = max_node + 1
        max_node += 1
        for ind in range(len(node_list)):
            k = node_list[ind]
            if k != i and k != j:
                d_ik = dist["%d,%d" % (i, k)] if i < k else \
                    dist["%d,%d" % (k, i)]
                d_jk = dist["%d,%d" % (j, k)] if j < k else \
                    dist["%d,%d" % (k, j)]
                dist["%d,%d" % (k, m)] = (d_ik + d_jk - dist["%d,%d" % (i, j)]) / 2

        # ---------- End your code -------------
   
        # Add the new node m to the Newick format representation of the tree
        # with edges of lengths 
        # dim = (dist[i,j] + avg_dist[i] - avg_dist[j])/2
        # djm = dist[i,j] - d[i,m], 
        # joining m to i and j
        
        if dist["%d,%d" % (i, j)] > 0:
            d_im = (dist["%d,%d" % (i, j)] + avg_dist[i] - avg_dist[j]) / 2
            d_jm = dist["%d,%d" % (i, j)] - d_im
        else:
            d_im = d_jm = 0

        newick[m] = ("(" + newick[i] + ":" + "%.7f" % d_im + ","
                     + newick[j] + ":" + "%.7f" % d_jm + ")")

        # Remove i and j from node_list and add m
        temp = []
        for idx in range(0, len(node_list)):
            
            if node_list[idx] != i and node_list[idx] != j:
                temp.append(node_list[idx])
   
        temp.append(m)
        
        node_list = list(temp)
        
        # Update the r terms, based on changes rather than recomputing from scratch
        if len(node_list) > 2:
            avg_dist[m] = 0
            
            for ind in range(0, len(node_list)-1):
                
                k = node_list[ind]
                avg_dist[k] = avg_dist[k] * (len(node_list)-1)
                avg_dist[k] -= dist["%d,%d" % (k, i)] if k < i \
                    else dist["%d,%d" % (i, k)]
                avg_dist[k] -= dist["%d,%d" % (k, j)] if k < j \
                    else dist["%d,%d" % (j, k)]
                avg_dist[k] += dist["%d,%d" % (k, m)]

                avg_dist[k] /= len(node_list)-2
                avg_dist[m] += dist["%d,%d" % (k, m)]

            avg_dist[m] = avg_dist[m] / (len(node_list)-2)
        
        # Remove any elements from the dict that contain nodes i or j
        delete_from_dict(dist, i, j)
        delete_from_dict(D, i, j)
        delete_from_dict(newick, i, j)
        delete_from_dict(avg_dist, i, j)

    # Return the Newick representation, joining together the final two nodes
    return ("(" + newick[node_list[0]] + ":" + 
            "%.7f" % (list(dist.values())[0]) +
            "," + newick[node_list[1]] + ":0);\n")


def summarize_alignment(seq1, seq2):
    """
    Summarize the alignment between two sequences by computing the number of
    matches, mismatches, and gaps. This code will contain similar logic to 
    the provided `compute_dist` function.

    Note: that we performed multiple sequence alignment to obtain the 
    aligned sequences in students.aligned.fasta. So, for any pair of sequences, 
    you may find a gap at the same place in the two aligned sequences. Gaps 
    should only be counted if they are matched with a non-gap character 
    (ignore a gap aligned to a gap).

    Args:
        seq1 (str): the first sequence, extracted from a multiple sequence
                    alignment
        seq2 (str): the second sequence, extracted from a multiple sequence
                    alignment

    Returns:
        a tuple of the number of (matches, mismatches, gaps) between the two
        sequences
    """

    #
    # YOUR CODE HERE
    #
    mismatch = 0
    match = 0
    gap = 0
    for i in range(len(seq1)):
        if seq1[i] == "-" and seq2[i] == "-":
            continue
        elif seq1[i] == "-" or seq2[i] == "-":
            gap += 1
        elif seq1[i] == seq2[i]:
            match += 1
        else:
            mismatch += 1

    # return the number of matches, mismatches and gaps as a tuple
    return match, mismatch, gap

########################################################################
# Provided functions for this problem
########################################################################


def compute_dist(seq1, seq2):
    """Returns the distance between two sequences. The distance is computed
    as the ratio between the number of mismatches and the total number
    of matches or mismatches.

    Args:
        seq1 (string) - first sequence
        seq2 (string) - second sequence

    Returns:
        the ratio of mismatches over the total number of matches or mismatches
        as a float
    """
    mismatch = 0
    match_or_mismatch = 0
    
    for i in range(len(seq1)):
        if seq1[i] == "-" or seq2[i] == "-":
            continue
        elif seq1[i] == seq2[i]:
            match_or_mismatch += 1
        else:
            mismatch += 1
            match_or_mismatch += 1

    return float(mismatch)/match_or_mismatch


def print_dist(dist):
    """
    Print the distance table
    """

    idx = [int(i.split(",")[0]) for i in list(dist.keys())]
    idx.extend([int(i.split(",")[1]) for i in list(dist.keys())])
    max_idx = max(idx)

    print("\t", end=" ")
    for col in range(2, max_idx + 1):
        print("{:>7}".format(col), end=" ")
    print() 

    for row in range(1, max_idx):
        print("%d\t" % row, end=" ")
        for col in range(2, row+1):
            print("       ", end=" ")
        for col in range(row+1, max_idx + 1):
            print("{:>7.4f}".format(dist[str(row)+","+str(col)]), end=" ")
        print() 

########################################################################
# Functions used by Neighbor Joining algorithm
########################################################################


def delete_from_dict(dictionary, i, j):
    """Deletes the dict entries with keys that contain i or j."""
      
    for k in list(dictionary.keys()):
        ks = [int(_) for _ in str(k).split(",")]
        if i in ks or j in ks:
            del dictionary[k]


def min_in_dict(wiki):
    """Returns the key associated with the minimum value in the dict."""
    import operator
    return min(iter(wiki.items()), key=operator.itemgetter(1))[0]


def two_min_in_dict(dictionary):
    
    import operator
    sorted_dict = sorted(iter(dictionary.items()), key=operator.itemgetter(1))
    element = sorted_dict[0][0]  # get the first element of the tuple
    (i, j) = element.split(",")
    return int(i), int(j)

        
if __name__ == "__main__":
    build_tree()
