from generate_HMM_sequence import generate_HMM_sequence


def run_analyze_sequence(gen_seq_file):
    """Load the nucleotide sequence HMM file and generate a 100000 length sequence,
    then do some analysis of the results, including the average length in each state.

    Args:
        gen_seq_file: The name of the output file for the generated nucleotide sequence.
    """
    seq_length = 100000
    state_sequence, observed_sequence = generate_HMM_sequence("HMM.parameters.txt", seq_length)

    # Write your generated sequence to file. Report the states that prevailed whenever
    # TCGA was observed, and their frequencies when observing TCGA. Finally, report
    # the average length spent in each state across the entire sequence.
    #
    # YOUR CODE GOES HERE
    #
    fh = open(gen_seq_file, "w")
    fh.write("".join(state_sequence))
    fh.write("\n")
    fh.write("".join(observed_sequence))
    fh.write("\n")
    fh.close()
    subsequence = ["T", "C", "G", "A"]
    print("Count of different state sequences corresponding to observed sequence TCGA:")
    dict_print_helper(compute_state_frequencies(state_sequence, observed_sequence, subsequence))
    print()
    print("Average length the system remains in a state:")
    dict_print_helper(compute_average_length(state_sequence))


def compute_average_length(state_sequence):
    """Given a state sequence, return the average length in each state

    Arguments:
        state_sequence: generated sequence of states, represented as list of single-char strings

    Returns:
        a dictionary mapping the state name to the average length in the state.
        Example return:
        {
            "W": 5.5,
            "S": 4.5
        }
    """
    # Check the type of state_sequence
    if type(state_sequence) is not list:
        raise TypeError(f"The argument 'state_sequence' must be a list of strings. "
                        f"(received type {type(state_sequence)})")

    # Compute the average length in each state
    #
    # YOUR CODE HERE
    #

    # contains the total number of a state and the number of continuous state sequences
    my_dict = {}

    # using while loop instead of recursion to ge around max recursion depth
    index = 0
    while index < len(state_sequence):
        index = length_compute_helper(my_dict, state_sequence, index)

    # output
    res = {}
    for key in list(my_dict.keys()):
        res[key] = my_dict[key]["total"] / my_dict[key]["continuous"]
    return res


def dict_print_helper(my_dict):
    for key in list(my_dict.keys()):
        print(key + ": ", my_dict[key])
    return;


def length_compute_helper(dictionary, state_sequence, index):
    # sequence end reached
    if index >= len(state_sequence):
        return index
        # the state we are counting
    state = state_sequence[index]
    # create new states entry if not in dictionary
    if dictionary.get(state) is None:
        dictionary[state] = {
            "total": 0,
            "continuous": 1,
        }
    # increase continuous count if in dictionary
    else:
        dictionary[state]["continuous"] += 1

    while index < len(state_sequence) and state_sequence[index] == state:
        dictionary[state]["total"] += 1
        index += 1
    return index


def compute_state_frequencies(state_sequence, observed_sequence, subsequence):
    """Given the state and observed sequences, return the state sequences that
    emitted the query subsequence and frequency in which those state sequences
    sequences emitted the subsequence.

    Arguments:
        state_sequence (list of single-char strings): generated state sequence
        observed_sequence (list of single-char strings): generated observed sequence
        subsequence (list of single-char strings): the observed subsequence to count

    Returns:
        a dictionary mapping the state name to the frequency of observing the
        provided sequence. Example return:
        {
            "WWWW": 2,
            "WWWS": 1,
            ...
        }
    """

    # Check the types for each of the input arguments
    if type(state_sequence) is not list:
        raise TypeError(f"The argument 'state_sequence' must be a list of strings. "
                        "(received type {type(state_sequence)})")
    if type(observed_sequence) is not list:
        raise TypeError(f"The argument 'observed_sequence' must be a list of strings. "
                        "(received type {type(observed_sequence)})")
    if type(subsequence) is not list:
        raise TypeError(f"The argument 'subsequence' must be a list of strings. "
                        "(received type {type(subsequence)})")

    #
    # YOUR CODE HERE
    #

    # method of comparing sequence comes from https://miguendes.me/python-compare-lists
    # length of sequence
    k = len(subsequence)
    # places to look
    n = len(state_sequence) - k + 1
    my_dict = {}
    for i in range(n):
        # if found a match
        if observed_sequence[i:i + k] == subsequence:
            # states as a string
            states = "".join(state_sequence[i:i + k])
            # create new states entry if not in dictionary
            if my_dict.get(states) is None:
                my_dict[states] = 1
            # else increase frequency
            else:
                my_dict[states] += 1
    return my_dict


if __name__ == "__main__":
    """Main method call, do not modify"""
    run_analyze_sequence("nucleotide_sequence.txt")
