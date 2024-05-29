import sys
from math import log
from compsci260lib import get_fasta_dict


def run_viterbi():
    hmm_file = 'HMM.methanococcus.txt'
    input_file = 'bacterial.genome.fasta'

    print("Decoding the Viterbi path for %s using %s" % (input_file, hmm_file))

    vit_ret = viterbi_decoding(input_file, hmm_file)

    # Collect the segment counts for each state
    counts = count_segments(vit_ret)

    # Report the first 10 and last 10 segments of your decoding
    #
    # YOUR CODE HERE
    #
    print("First 10 segments:")
    for i in range(10):
        print("\"{}\", {}-{}".format(vit_ret[i]["state"], vit_ret[i]["start"], vit_ret[i]["end"]))
    print()
    print("Last 10 segments:")
    for i in range(-10, 0):
        print("\"{}\", {}-{}".format(vit_ret[i]["state"], vit_ret[i]["start"], vit_ret[i]["end"]))
    print()


    # Then report the number of segments that exist in each state.
    #
    # YOUR CODE HERE
    #
    print("The number of segments that exist in each state:")
    for key in list(counts.keys()):
        print("key: {}, number: {}".format(key, counts[key]))

def viterbi_decoding(input_file, hmm_file):
    """Calculate the Viterbi decoding of an input sequence

    Arguments:
        input_file (str): path to input fasta file
        hmm_file (str): path to HMM file

    Returns:
        A list of dictionaries of segments in each state (1-indexed).
        An example output may look like:

        [
            {‘start’: 1, ‘end’: 12, ‘state’: ‘S’},
            {‘start’: 13, ‘end’: 20, ‘state’: ‘W’},
            ...
        ]
    """

    # Open HMM description file
    try:
        f_hmm_file = open(hmm_file, 'r')
    except IOError:
        print("IOError: Unable to open HMM file: %s." % hmm_file)
        print("Exiting.")
        sys.exit(1)

    # Read the state names
    states = f_hmm_file.readline().split()
    K = len(states)
    
    # Read the initial probability vector (and log transform entries)
    probs = f_hmm_file.readline().split()
    initial_probs = [log(float(prob)) for prob in probs]
    
    # Read the transition matrix (and log transform entries)
    transitions = [None for _ in range(K)]
    for k in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [log(float(trans_prob)) for trans_prob in matrix_row_arry]
        transitions[k] = matrix_row
    
    # Read the emitted symbols
    emitted_symbols_list = f_hmm_file.readline().split()
    emitted_symbols = {symbol: index for index, symbol in enumerate(emitted_symbols_list)}

    # Read the emission probability matrix (and log transform entries)
    emit_probs = [None for _ in range(K)]
    for k in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [log(float(emit_prob)) for emit_prob in matrix_row_arry]
        emit_probs[k] = matrix_row
    
    f_hmm_file.close()
    
    seq_dict = get_fasta_dict(input_file)
    emit_str = list(seq_dict.values())[0]  # there's only 1
    
    print("Read a sequence of length", len(emit_str))
    
    # Create Viterbi table and traceback table
    viterbi = [[0 for _ in range(len(emit_str))] for _ in range(K)]
    pointers = [[0 for _ in range(len(emit_str))] for _ in range(K)]

    # Initialize the first column of the matrix
    for k in range(K):
        in_index = emitted_symbols[emit_str[0].upper()]
        viterbi[k][0] = emit_probs[k][in_index] + initial_probs[k]
    
    # Build the matrix column by column
    for i in range(1, len(emit_str)):
        in_index = emitted_symbols[emit_str[i].upper()]
        
        for l in range(K):
            # Compute the entries viterbi[l][i] and pointers[l][i]
            # Tip: Use float('-inf') for the value of negative infinity
            #
            # YOUR CODE HERE
            #

            # viterbi[k][i-1] + transitions[k][l] for all k
            candidates = [(viterbi[k][i-1] + transitions[k][l]) for k in range(K)]

            viterbi[l][i] = emit_probs[l][in_index] + max(candidates)
            # tie-break by find the lowest k such that viterbi[k][i-1] + transitions[k][l] is largest
            pointers[l][i] = candidates.index(max(candidates))

    # Traceback, stored as a list of segments in each state (represented using dictionaries)
    #
    # YOUR CODE HERE
    #


    # initialize list and entry point
    last_column = [viterbi[_][-1] for _ in range(K)]
    state_index = last_column.index(max(last_column))
    result = [{"start": len(emit_str), "end": len(emit_str), "state": states[state_index]}]

    for i in range(len(emit_str) - 1, 0, -1):
        # decrease start of current entry if still in the same segment
        if pointers[state_index][i] == state_index:
            result[-1]["start"] = result[-1]["start"]-1
        # add new entry if not in the same segment
        else:
            state_index = pointers[state_index][i]
            result.append({"start": i, "end": i, "state": states[state_index]})

    # reverse
    result.reverse()
    return result


def count_segments(vit_ret):
    """Calculate the number of segments appearing in each state of
    the viterbi path

    Arguments:
        vit_ret (list of dicts): dictionary of segments in each state.
            see: return value of viterbi_decoding

    Returns:
        a dictionary mapping states to number of segments of that state. 
        e.g. {'W': 10, 'S': 9}
    """

    #
    # YOUR CODE HERE
    #

    # new list simplifying the task
    aux = [entry["state"] for entry in vit_ret]

    res = {}
    for state in aux:
        # add entry if not in dictionary
        if res.get(state) is None:
            res[state] = 1
        # else increase count
        else:
            res[state] += 1

    return res


if __name__ == '__main__':
    """Call run_viterbi(), do not modify"""
    run_viterbi()
