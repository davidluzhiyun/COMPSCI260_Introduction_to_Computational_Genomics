from bwt import *
from fm_index import *
from compsci260lib import *


def align_patient_reads():
    """Align patient reads to each bacterial genome"""

    # Patients
    patients = ['patient1',
                'patient2',
                'patient3']

    # Bacterial species
    panel = ['Bacteroides_ovatus',
             'Bacteroides_thetaiotaomicron',
             'Bifidobacterium_longum',
             'Eubacterium_rectale',
             'Lactobacillus_acidophilus',
             'Peptoniphilus_timonensis',
             'Prevotella_copri',
             'Roseburia_intestinalis',
             'Ruminococcus_bromii',
             'Vibrio_cholerae']

    # Store the genome sequence and bwt structures for each bacterial species
    bact_sequences = {}
    bact_bwt_structures = {}
    for bacteria in panel:
        # For each of the bacteria in our panel, create a dictionary entry
        # where keys are bacterial names and values are their genome sequences.
        bact_sequences[bacteria] = list(get_fasta_dict(
            'reference_genomes/%s.fasta' % bacteria).values())[0]

        # For each of the bacterial genome sequences, create a dictionary entry
        # where keys are bacterial names and values are their BWT data
        # structures.
        bact_bwt_structures[bacteria] = make_all(bact_sequences[bacteria])

    # Store a mapping of patient names to reads
    patient_reads = {}
    for patient in patients:
        reads = list(get_fasta_dict('patients/%s.fasta' % patient).values())
        patient_reads[patient] = reads

    # Store the reads mapped per bacterial species per patient
    mapped_patient_reads = {}

    # Consider all patients
    for patient in patients:
 
        # Find uniquely mapped reads for each bacteria for the patient
        # and store the read start positions
        mapped_reads = find_aligned_reads_for_patient(
            patient_reads[patient], bact_bwt_structures)
        mapped_patient_reads[patient] = mapped_reads

    # Report the microbe prevalences for each of your patients
    # 
    # YOUR CODE GOES HERE
    #

    # Cycle through each patient and bacteria for the number of unique counts
    counting_board = {}
    for patient in patients:
        counting_board[patient] = {}
        unique_reads = 0
        # first cycle for the counts
        for bacteria in panel:
            count = len(mapped_patient_reads[patient][bacteria])
            counting_board[patient][bacteria] = count
            unique_reads += count
        # second cycle for calculating prevalence
        for bacteria in panel:
            counting_board[patient][bacteria] = counting_board[patient][bacteria] / unique_reads

    # Print
    for patient in patients:
        print(patient + ": ")
        print("Prevalence:")
        for bacteria in panel:
            print((bacteria.replace("_", " ") + ": {}").format(counting_board[patient][bacteria]))
        print()

    # Use `read_mapper` and `longest_zeroes` to identify unmapped regions
    # for the relevant patients and species (questions 2f-h)
    # 
    # YOUR CODE GOES HERE
    #

    # patient 1
    res1 = longest_zeros(read_mapper(mapped_patient_reads["patient1"]['Vibrio_cholerae'], bact_sequences['Vibrio_cholerae']))
    # patient 2
    res2 = longest_zeros(read_mapper(mapped_patient_reads["patient2"]['Vibrio_cholerae'], bact_sequences['Vibrio_cholerae']))

    # print (With checking)
    if res1 is not None:
        print("Longest zeros for patient1 (Vibrio cholerae): {}-{}".format(res1[0], res1[1]))
    else:
        print("Patient 1's vector doesn't have internal strings of zero, assumption failed")
    if res2 is not None:
        print("Longest zeros for patient2 (Vibrio cholerae): {}-{}".format(res2[0], res2[1]))
    else:
        print("Patient 2's vector doesn't have internal strings of zero")
    print()

    # report longest missing sequence
    print("longest missing sequence patient1:")
    missing_sequence = bact_sequences['Vibrio_cholerae'][res1[0]: res1[1]+1]
    for i in range(0, len(missing_sequence), 60):
        print(missing_sequence[i:min(i+60, len(missing_sequence))])

def find_aligned_reads_for_patient(reads, bact_bwt_structures):
    """
    Given a list of reads for a patient, identify the reads that uniquely map
    to each bacteria's genome using its relevant BWT data structure. Reads that
    are mapped to a bacteria's genome should be stored as starting positions in
    a list.

    Args:
        reads (list of str):
            mapping a patient's read names (str) to read sequences (str).

        bact_bwt_structures: dictionary mapping bacterial names (str) to 
            structures required for efficient exact string matching). Refer
            to the return tuple from `make_all` in fm_index.py.

    Returns:
        a dictionary mapping bacterial names (str) to the start positions of
        reads mapped to that bacteria's genome. Note that the end positions are
        not needed as the reads are all 50 bases long. Start positions should
        be stored using 0-indexing.

        Example return structure:
        {
            'Bacteroides_ovatus': [8, 124, 179, ...],
            ...
        }
    """

    counts = {}
    panel = list(bact_bwt_structures.keys())

    # 
    # YOUR CODE GOES HERE
    #

    # initialize counts
    # for each species of bacteria
    for bacterial_name in panel:
        counts[bacterial_name] = []

    # for each read
    for read in reads:
        # reverse_complement read because the bacterial genomes aren't passed into the function
        c_read = reverse_complement(read)
        # Entry for storing bacterial_name and place of finding
        # also check if the read is unique
        entry = []
        # for each species of bacteria
        for bacterial_name in panel:
            r = find((c_read), bact_bwt_structures[bacterial_name])
            # first find
            if r != [] and entry == []:
                entry = [bacterial_name, r[0]]
            # duplicated find
            elif r != [] and entry != []:
                entry = []
                break
            # do nothing if no find yet
        # unique find
        if entry != []:
            counts[entry[0]].append(entry[1])

    # sort result
    # for each species of bacteria
    for bacterial_name in panel:
        counts[bacterial_name] = sorted(counts[bacterial_name])


    return counts


def read_mapper(starting_positions, genome):
    """
    Using the starting positions of reads that were aligned to a bacterial
    genome, construct a count vector (as a list) that counts how many reads
    were aligned to a position in the genome. The vector's size will be the 
    length of the genome. You may assume that each read is 50 base pairs long.

    Args:
        starting_positions (list of ints): 
            starting positions of reads that were aligned to a genome.

        genome (str): the genomic nucleotide sequence to which the reads 
                      were aligned.

    Returns:
        (list of ints): vector of aligned read counts to the genome.
        i.e. [c_1, c_2, ..., c_i, ..., c_n], where n=length of the genome
        and c_i = the count of aligned reads for the patient at genome
        position i.
    """

    # 
    # YOUR CODE GOES HERE
    #

    # initialize
    count_vector = [0 for i in range(len(genome))]

    for s in starting_positions:
        # increase 50 positions one
        # no need to handle out of bound situation because reads are exact matches
        for i in range(50):
            count_vector[s + i] += 1

    return count_vector

# It may be helpful to read the documentation for the methods
# given below, but you will NOT have to make any changes to
# them in order to complete the problem set.


def longest_zeros(count_vector):
    """Given a count vector, return the start and stop position (inclusive) of
    the longest string of internal zeros in the vector. If there is no
    internal string of zeros, return None.

    Examples to understand behavior:
    input -> output
    contain valid internal string of zeros:
    [1, 1, 1, 0, 0, 1, 1] -> (3, 4)
    [1, 1, 1, 0, 1, 1, 1]  -> (3, 3)
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0] -> (5, 6)

    do not contain internal string of zeros:
    [0, 0, 0, 1, 1, 1, 1] -> None
    [1, 1, 1, 1, 0, 0, 0] -> None
    [0, 0, 0, 0, 0, 0, 0] -> None
    [1, 1, 1, 1, 1, 1, 1] -> None

    Args:
        count_vector (list of ints): vector of aligned read counts to the
        genome.  see: the return value for `read_mapper()`

    Returns:
        (tuple of (int, int)): the start and stop position (inclusive) of the longest
        internal string of zeros in the count_vector. If there are no internal
        runs-of-zero the return will be None.
    """

    zero_nums = []
    genome_len = len(count_vector)
    for i in range(0, genome_len):
        if count_vector[i] == 0:
            zero_nums.append(i)

    if len(zero_nums) == 0:
        return None

    counter = 1
    longest_run = {}
    longest_run[1] = []
    longest_run[1].append(zero_nums[0])
    for z in zero_nums[1:]:
        if (z - longest_run[counter][-1]) == 1:
            longest_run[counter].append(z)
        else:
            counter += 1
            longest_run[counter] = []
            longest_run[counter].append(z)

    for run in list(longest_run.keys()):
        if 0 in longest_run[run] or genome_len-1 in longest_run[run]:
            del longest_run[run]

    longest = []
    for run in list(longest_run.values()):
        if len(run) > len(longest):
            longest = run

    # There was no run of zeroes found, return None
    if len(longest) == 0:
        return None

    start = longest[0]
    stop = longest[-1]

    # Return the start and end positions of the longest zeroes (0-indexed)
    return start, stop


if __name__ == '__main__':
    align_patient_reads()
