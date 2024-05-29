import os
import random


def generate_HMM_sequence(hmm_file, seq_length):
    """Load an HMM specification from file, and generate state and observed
    sequences through sampling of the HMM.

    The HMM will have states labeled as strings and observations as characters
    which will be useful when we generate an HMM with nucleotide sequence
    observations.

    An example return sequence may look like:
        (["W", "S", "W"], ["A", "T", "G"]) or
        (["F", "L", "L"], ["2", "6", "6"])

    Arguments:
        hmm_file (str): path to the HMM file
        seq_length (int): the length of the sequence we will generate

    Returns:
        a tuple containing two lists of strings, with the first list storing
        the sequence of states (which are arbitrary strings) and the second
        list storing the sequence of observations (which are assumed to be
        single-character strings):

        (state sequence as a list of strings,
         observed sequence as a list of single-character strings)
    """

    if not os.path.exists(hmm_file):
        print("Can't open HMM parameter file: %s" % hmm_file)
        return -1

    f = open(hmm_file, "r")

    # read the state names
    states = f.readline().strip().split()

    # read the initial probabilities
    initial_probs = f.readline().strip().split()
    initial_probs = [float(p) for p in initial_probs]

    # read the transition matrix
    transitions = {}
    for i in range(0, len(states)):
        state = states[i]
        matrix_row = f.readline().strip().split()
        transitions[state] = [float(p) for p in matrix_row]

    # read the input alphabet
    input_alphabet = f.readline().strip().split()

    # read the emission matrix
    emission = {}
    for i in range(0, len(states)):
        state = states[i]
        matrix_row = f.readline().strip().split()
        emission[state] = [float(p) for p in matrix_row]
        # normalize
        sum_emission = sum(emission[state])
        emission[state] = [x / sum_emission for x in emission[state]]
    f.close()

    #
    # YOUR CODE HERE
    #

    # edge case
    if seq_length == 0:
        return ([], [])
    # initialization
    state_seq = random.choices(states, weights=initial_probs, k=1)
    observed_seq = random.choices(input_alphabet, weights=emission[state_seq[0]], k=1)
    for _ in range(seq_length - 1):
        state_seq.append(random.choices(states, weights=transitions[state_seq[-1]], k=1)[0])
        observed_seq.append(random.choices(input_alphabet, weights=emission[state_seq[-1]], k=1)[0])
    return (state_seq, observed_seq)  # a tuple containing the state and observation sequences



