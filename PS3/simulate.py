import sys
import random
from compsci260lib import *


def run_simulate():
    """
    Simulates the sequencing process then empirically compute and report 
    the quantities from parts a-c.
    """

    iterations = 20
    G = 3 * (10 ** 6)
    R = 4 * (10 ** 4)
    L = 400

    # Call simulate(G, R, L) `iteration` times. Report the empirical values 
    # from parts a-c for each iteration
    #
    # YOUR CODE HERE
    #

    # keep a sum for averaging
    sum_of_results = [0, 0, 0, 0]
    print("All floating point results truncated to the 2 decimal place")
    for i in range(iterations):
        t = simulate(G, R, L)
        # for float print to 2 decimal place
        # for integers just print the integer part
        print('''
Simulation {}
The empirical coverage: {:0.2f}
The number of nucleotides not covered by any read: {}
The number of contigs: {}
The average length of these contigs: {:0.2f}
        '''.format(i + 1, t[0], int(t[1]), int(t[2]), t[3]))
        for j in range(4):
            sum_of_results[j] += t[j]
    print('''
Average
The empirical coverage: {:0.2f}
The number of nucleotides not covered by any read: {:0.2f}
The number of contigs: {:0.2f}
The average length of these contigs: {:0.2f}
    '''.format(sum_of_results[0]/iterations, sum_of_results[1]/iterations, sum_of_results[2]/iterations, sum_of_results[3]/iterations))


def simulate(G, R, L):
    """
    Simulates one iteration of the sequencing process and empirically compute 
    the empirical coverage (average number of times a nucleotide in the genome
    was sequenced), the number of nucleotides not covered by any read, the 
    number of contigs assuming you can use the oracular assembly algorithm to
    assemble all the reads, and the average length of these contigs.

    Args:
        G (int) - the length of the genome
        R (int) - the number of reads
        L (int) - the length of each read

    Returns
        a tuple of floats:

            (Empirical coverage, 
             Number of nucleotides not covered by any read, 
             Number of contigs,
             Average length of these contigs)
    """

    #
    # YOUR CODE HERE
    #

    # Initialization of genome
    genome = [0 for i in range(G)]

    # R number of reads
    for i in range(R):
        # start index selected from 0 to G - L
        read_start = random.randint(0, (G - L))
        # increment L elements
        for j in range(L):
            genome[j + read_start] += 1

    # total covers
    covers = 0

    # total number of uncovered nucleotides
    zero_count = 0

    # total number of contigs
    contigs = 0

    for i in range(G):
        covers += genome[i]
        if genome[i] == 0:
            zero_count += 1
            # conditional to process gaps larger than one nucleotide long
            # and special case where genome starts with nucleotides not covered
            if (i > 0) and (genome[i - 1] != 0):
                contigs += 1
    # If the last nucleotide is part of a contig, there is one more contig yet to be counted
    if genome[-1] != 0:
        contigs += 1

    coverage = covers / G
    average_contig_length = (G - zero_count) / contigs

    return (coverage, float(zero_count), float(contigs), average_contig_length)


if __name__ == '__main__':
    """Call run_simulate(), do not modify"""
    run_simulate()
