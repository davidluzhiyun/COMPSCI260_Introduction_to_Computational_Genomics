from functools import cmp_to_key

from compsci260lib import *


# Note that the '$' character will be used to designate the end of a given
# string.


def solve_bwt():
    """Load the mystery.txt file and decode its contents using the
    reverse BWT transformation. Report the decoded contents."""

    # Example sequences for forward_bwt() and reverse_bwt();
    # you may change them to different sequences to test your code.
    """
    seq1 = 'GATTACA$'
    seq2 = 'ACTGA$TA'
    forward_bwt(seq1)
    reverse_bwt(seq2)
    """

    # Code to open the file mystery.txt in the correct encoding
    # across platforms, and read its contents into a variable.
    """
    with open('mystery.txt', 'r', encoding='UTF-8') as f:
         mystery_seq = f.read()
    """
    #
    # YOUR CODE GOES HERE
    #

    # Code to report Apply d)
    s = "CGGACTAACGGACTAACGGACTAACGGACTAC$"
    r = forward_bwt(s)
    print("BWT: {} -> {}\n".format(s, r))

    # Code to report Apply e)
    # open
    with open('mystery.txt', 'r', encoding='UTF-8') as f:
        mystery_seq = f.read()
    # decode
    decoded_seq = reverse_bwt(mystery_seq)

    # process the decoded sequence for pretty printing

    # split the words
    words = (decoded_seq[1:]).split("_")

    # Abouts 60 characters per line
    linelength = 60

    # switch line when length of the line exceed 60
    # always finish current word
    text = ""
    counter = 0
    for word in words:
        # add in the word and a space
        text = text + word + " "
        counter += len(word) + 1
        # switch line when length of the line exceed 60
        if counter >= linelength:
            counter = 0
            text = text + "\n"

    # print
    print(text)


def forward_bwt(seq):
    """forward_bwt(seq) takes as input a string containing the EOF character to
    which the BWT must be applied. The method should then return the result of
    the BWT on the input string.

    For example:
        forward_bwt('GATTACA$') --> 'ACTGA$TA'

    Args:
        seq (str): input string with an EOF character

    Returns:
        (str): the transformed string
    """

    #
    # YOUR CODE GOES HERE
    #

    # rotate
    matrix = rotate(seq)

    # sort
    # inspired by
    # https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python
    # https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
    matrix = sorted(matrix, key=cmp_to_key(custom_compare))

    # extract final column
    result = ""
    for row in matrix:
        result = result + row[-1]

    return result


# Auxiliary function for sorting
# design inspired by
# https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python
# https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
# https://stackoverflow.com/questions/22490366/how-to-use-cmp-in-python-3
# ommited cases not present in our problem
def custom_compare(a, b):
    if a[0] == b[0]:
        if len(a) > 1:
            return custom_compare(a[1:], b[1:])
        else:
            return 0
    if b[0] == "$":
        return 1
    if a[0] == "$":
        return -1
    return default_cmp(a[0], b[0])


# default compare function re-introduced
# https://stackoverflow.com/questions/22490366/how-to-use-cmp-in-python-3
def default_cmp(a, b):
    return (a > b) - (a < b)


# Auxiliary function for rotation
def rotate(string):
    result = []
    for i in range(len(string)):
        result.append(string[i:] + string[:i])
    return result


def reverse_bwt(seq):
    """reverse_bwt(seq) takes as input a string containing the EOF character to
    which the reverse of the BWT must be applied. The method should then return
    the result of the reversal on the input string.

    For example:
        reverse_bwt('ACTGA$TA') --> 'GATTACA$'

    Args:
        seq (str): input string with an EOF character

    Returns:
        (str): the transformed string
    """

    #
    # YOUR CODE GOES HERE
    #

    # initialize
    matrix = ["" for i in range(len(seq))]

    # included the intial sorting as one append and sort operation to an empty matrix
    for i in range(len(seq)):
        matrix = apd(seq, matrix)
        matrix = sorted(matrix, key=cmp_to_key(custom_compare))

    # return the first row

    return matrix[0]


# Auxiliary function for appending
# a is the sequence, b is a array of strings
def apd(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result


if __name__ == '__main__':
    """Run solve_bwt(). Do not modify this code"""
    solve_bwt()
