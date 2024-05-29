import sys
from math import log, exp

import viterbi
from compsci260lib import get_fasta_dict


def run_posterior():
    input_file = "bacterial.genome.fasta"
    hmm_file = "HMM.methanococcus.txt"

    posterior = posterior_decoding(input_file, hmm_file)

    # Report the first and last ten segments in your decoding
    #
    # YOUR CODE HERE
    #
    counts = viterbi.count_segments(posterior)
    print("First 10 segments:")
    for i in range(50):
        print("\"{}\", {}-{}".format(posterior[i]["state"], posterior[i]["start"], posterior[i]["end"]))
    print()
    print("Last 10 segments:")
    for i in range(-50, 0):
        print("\"{}\", {}-{}".format(posterior[i]["state"], posterior[i]["start"], posterior[i]["end"]))

    print()

    print("The number of segments that exist in each state:")
    for key in list(counts.keys()):
        print("key: {}, number: {}".format(key, counts[key]))


def posterior_decoding(input_file, hmm_file):
    """
    Calculate the posterior decoding and return the decoded segments.

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
    
    print("Done reading sequence of length ", len(emit_str))
    
    # Run the forward algorithm
    forward = run_forward(states, initial_probs, transitions, emitted_symbols,
        emit_probs, emit_str)

    # Run the backward algorithm
    backward = run_backward(states, initial_probs, transitions, 
        emitted_symbols, emit_probs, emit_str)

    # Calculate the posterior probabilities
    # Initializing the posterior 2D matrices
    posterior = [[0 for _ in range(len(emit_str))] for _ in range(K)]
    for i in range(len(emit_str)):
        # Did not normalize the probabilities (i.e., did not divide by P(X)),
        # because we will only use these probabilities to compare
        # posterior[0][i] versus posterior[1][i]
        for k in range(K):
            posterior[k][i] = forward[k][i] + backward[k][i]
    
    # Create the list of decoded segments to return
    #
    # YOUR CODE HERE
    #

    first_column = [posterior[_][0] for _ in range(K)]
    state_index = first_column.index(max(first_column))
    result = [{"start": 1, "end": 1, "state": states[state_index]}]

    for i in range(len(emit_str)):
        # decrease start of current entry if still in the same segment
        column = [posterior[_][i] for _ in range(K)]
        new_state_index = column.index(max(column))
        if new_state_index == state_index:
            result[-1]["end"] += 1
        else:
            state_index = new_state_index
            result.append({"start": i+1, "end": i+1, "state": states[state_index]})

    return result


def run_forward(states, initial_probs, transitions, emitted_symbols, 
                emit_probs, emit_str):
    """Calculates the forward (log) probability matrix.

    Arguments:
        states (list of str): list of states as strings
        initial_probs (list of float): list of log(initial probabilities) for each
            state
        transitions (list of list of float): matrix of log(transition probabilities)
        emitted_symbols (dict {str: int}): dictionary mapping emitted symbols to their index
        emit_probs (list of list of float): matrix of log(emission probabilities)
            for each state and emission symbol
        emit_str (str):

    Returns:
        (list of list of floats): matrix of forward (log) probabilities
    """

    K = len(states)
    N = len(emit_str)
    
    forward = [[0 for _ in range(N)] for _ in range(K)]
    
    # Initialize
    emit_index = emitted_symbols[emit_str[0].upper()]
    for k in range(K):
        forward[k][0] = initial_probs[k] + emit_probs[k][emit_index]

    # Iterate
    for i in range(1, N):
        emit_index = emitted_symbols[emit_str[i].upper()]

        # Compute the forward probabilities for the states
        #
        # YOUR CODE HERE
        #
        for l in range(K):
            terms = [(emit_probs[l][emit_index]+forward[k][i - 1] + transitions[k][l]) for k in range(K)]
            forward[l][i] = sum_log_list(terms)

    return forward


# helper function to calculate log(p + q) from log(p) and log(q)
def sum_log(log_p, log_q):
    return log_p + log(1 + exp(log_q - log_p))


def sum_log_list(terms):
    if len(terms) < 2:
        return terms[0]
    else:
        sum_so_far = sum_log(terms[0], terms[1])
        for i in range(2, len(terms)):
            sum_so_far = sum_log(sum_so_far, terms[i])
        return sum_so_far


def run_backward(states, initial_probs, transitions, emitted_symbols,
                 emit_probs, emit_str):
    """Calculates the backward (log) probability matrix.

        Arguments:
            states (list of str): list of states as strings
            initial_probs (list of float): list of log(initial probabilities) for
                each state
            transitions (list of list of float): matrix of log(transition
                probabilities)
            emitted_symbols (dict {str: int}): dictionary mapping emitted symbols to their index
            emit_probs (list of list of float): matrix of log(emission
                probabilities) for each state and emission symbol
            emit_str (str):

        Returns:
            (list of list of floats): matrix of backward (log) probabilities
    """

    
    K = len(states)
    N = len(emit_str)

    backward = [[0 for _ in range(N)] for _ in range(K)]

    # Initialize
    for k in range(K):
        backward[k][N - 1] = log(1)  # which is zero, but just to be explicit...

    # Iterate
    for i in range(N - 2, -1, -1):
        emit_index = emitted_symbols[emit_str[i + 1].upper()]

        # Compute the backward probabilities for the states
        #
        # YOUR CODE HERE
        #
        for k in range(K):
            terms = [(emit_probs[l][emit_index]+backward[l][i + 1] + transitions[k][l]) for l in range(K)]
            backward[k][i] = sum_log_list(terms)

    return backward


if __name__ == '__main__':
    """Call run_posterior(), do not modify"""
    run_posterior()
