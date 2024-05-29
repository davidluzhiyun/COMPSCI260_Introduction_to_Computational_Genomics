import math
import random
import timeit
#added pandas to print the table
# removed for autograder to run
#import pandas



# random_list needs to be available as a global variable
# for the timeit function to work properly
random_list = None


def brute_force(score_list):
    """Get the maximum similarity score using brute force.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """

    #
    # Your code goes here
    #

    # initialize possible max value to - math.inf
    max_value = -math.inf

    for start in range(len(score_list)):
        # cycles the starting index(inclusive) through the list
        # initialize the sum of the sublist to 0 each outer cycle
        sublist_sum = 0
        for end in range(start, len(score_list)):
            # add new element to sum
            sublist_sum += score_list[end]
            if sublist_sum > max_value:
                max_value = sublist_sum
    return max_value  # replace with the computed maximal score


def divide_conquer(score_list):
    """Get the maximum similarity score using divide and conquer.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """

    #
    # Your code goes here
    #

    # mid is the ending index (exclusive) of the left half and starting index of the right half(inclusive)
    # By checking against small cases where length is 2 or 3, I have found that my design of mid ensures:
    # The base case is always one element long and mid doesn't go out of bound
    # There are always at least one element to the left of mid, but mid might be the rightest element
    mid = (int(len(score_list) / 2))

    # Base case
    if len(score_list) == 1:
        return score_list[0]

    # max sum for sublists on the left
    max_l = divide_conquer(score_list[0: mid])

    # max sum for sublists on the left
    max_r = divide_conquer(score_list[mid: len(score_list)])

    # For the crossing max sublist, the left side excluding mid and the right side including mid should both be
    # as large as possible.
    # The choice of inclusion and exclusion is based on the previously mentioned property of mid.
    # Empty lists are assigned sum -infinity instead of 0 to prevent returning 0 for an empty sublist for an entirely
    # negative score_list.

    # sum of the left side of the crossing sublist with max sum
    max_m_l = -math.inf
    l_sum = 0
    for i in range(mid - 1, -1, -1):
        l_sum += score_list[i]
        if l_sum > max_m_l:
            max_m_l = l_sum

    # sum of the right side of the crossing sublist with max sum
    max_m_r = -math.inf
    r_sum = 0
    for i in range(mid, len(score_list), 1):
        r_sum += score_list[i]
        if r_sum > max_m_r:
            max_m_r = r_sum

    # The final calculated max sum for crossing sublist
    max_m = max_m_l + max_m_r
    # Compare
    max_all = max(max_l, max_r, max_m)
    return max_all  # replace with the computed maximal score


def linear(score_list):
    """Get the maximum similarity score in linear time.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """

    #
    # Your code goes here
    #
    MAX_SO_FAR = -math.inf
    MAX_INCLUDING_HERE = -math.inf
    for elem in score_list:
        MAX_INCLUDING_HERE = max(MAX_INCLUDING_HERE + elem, elem)
        MAX_SO_FAR = max(MAX_INCLUDING_HERE, MAX_SO_FAR)

    return MAX_SO_FAR  # replace with the computed maximal score


def run_collective_similarity():
    """
    Run collective similarity and collect timing for each algorithm.

    Note: there is no reporting in this problem, `brute_force`,
    `divide_conquer`, and `linear` will be evaluated for correctness.
    """

    # Declare random_list as the same global variable defined
    # on line 7 above for use in the timeit library below.
    global random_list

    # You can use this to test the correctness of your code by using
    # sample_list as an input to each function.  You could also consider
    # creating other sample lists as tests, including a test case where
    # the right answer of zero occurs when an empty list would be optimal.

    sample_list = [2, -3, -4, 4, 8, -2, -1, 1, 10, -5]

    brute_force(sample_list)
    divide_conquer(sample_list)
    linear(sample_list)

    # This part below is used to test the runtime of your code, an example is
    # given below for brute force algorithm with a random list of length 100.
    # You will have to measure the runtime of each algorithm on every input size
    # given in the problem set.

    """
    allowed_scores = [i for i in range(-10, 11)]
    random_list = [random.choice(allowed_scores) for _ in range(100)]
    bruteforce_runtime = timeit.timeit("brute_force(random_list)",
                                       setup="from __main__ import brute_force, random_list",
                                       number=1)
    """
    # table inspired by https://learnpython.com/blog/print-table-in-python/
    allowed_scores = [i for i in range(-10, 11)]
    my_columns = ["brute force runtime", "divide & conquer runtime", "linear runtime"]
    my_index = ["10^" + str(i) for i in range(2, 9)]
    table = []
    for i in range(2, 9):
        length = int(math.pow(10, i))
        random_list = [random.choice(allowed_scores) for _ in range(length)]
        bruteforce_runtime = "N/A"
        divideconquer_runtime = "N/A"
        if i <= 5:
            bruteforce_runtime = timeit.timeit("brute_force(random_list)",
                                               setup="from __main__ import brute_force, random_list",
                                               number=1)
        if i <= 7:
            divideconquer_runtime = timeit.timeit("divide_conquer(random_list)",
                                                  setup="from __main__ import divide_conquer, random_list",
                                                  number=1)
        linear_runtime = timeit.timeit("linear(random_list)",
                                       setup="from __main__ import linear, random_list",
                                       number=1)
        table.append([bruteforce_runtime, divideconquer_runtime, linear_runtime])
    # For printing out the table. needs pandas to run.
    # removed for autographing
    # df = pandas.DataFrame(table, columns = my_columns, index = my_index)
    # print(df)


if __name__ == "__main__":
    """Run run_collective_similarity(). Do not modify this code"""
    run_collective_similarity()
