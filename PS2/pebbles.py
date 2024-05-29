def solve_pebbles(grid_file):
    """Code for the "Pebble Beach" problem. This problem involves implementing
    an O(n) dynamic programming algorithm for computing the maximum value of
    the placement of pebbles under the constraint that no pebbles can be
    vertically or horizontally adjacent.

    Args: grid_file (str): a string with the name of the file that contains
          the grid of values. Each line of that file should contain a row
          of four integers, separated by tabs

    Returns: the maximal score for the optimal pebble placements
    """

    #
    # Your code goes here
    #

    # patterns at their assigned index
    pattern = [[1, 0, 1, 0],
               [1, 0, 0, 1],
               [0, 1, 0, 1],
               [1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1],
               [0, 0, 0, 0]]

    # The compatible patterns for each pattern
    compatibles = [[2, 4, 6, 7],
                   [4, 5, 7],
                   [0, 3, 5, 7],
                   [2, 4, 5, 6, 7],
                   [0, 1, 3, 5, 6, 7],
                   [1, 2, 3, 4, 6, 7],
                   [0, 3, 4, 5, 7],
                   [0, 1, 2, 3, 4, 5, 6, 7]]

    # open file
    fh = open(grid_file, "r")

    # initialize the maximum values of the total patterns given the valid patterns
    # on the last row Tk[p]
    t = [0 for i in range(8)]

    for line in fh:
        # Parse the line into lists of 4 integers
        row = [int(token) for token in line.split()]

        # calculate the values for the current row given valid patterns on it
        r = [sum([row[i] * pattern[p][i] for i in range(4)]) for p in range(8)]

        # Update Tk[p] for each p
        new_t = [max([t[compatible] + r[p] for compatible in compatibles[p]]) for p in range(8)]
        t = new_t
    # Final comparison
    result = max(t)
    #  Return the maximum value of the placement of pebbles
    return result


def run_pebbles():
    """Run solve pebbles, you may try and create different grid files to debug
    that match the formatting of grid.txt (tab separated values)

    Note: there is no reporting in this problem, only `solve_pebbles` will
    be evaluated for correctness.
    """
    max_score = solve_pebbles('grid.txt')
    print("The max score for this grid is %d" % max_score)


if __name__ == '__main__':
    """Run run_pebbles(). Do not modify this code"""
    run_pebbles()
