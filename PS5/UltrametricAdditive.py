from math import sqrt

from compsci260lib import *


def solve_ultrametric_additive():
    
    # Distance metrics for table 1 and table 2
    dist_1 = {"1,2" : 0.3, "1,3" : 0.7, "1,4" : 0.7,
              "2,3" : 0.6, "2,4" : 0.6,
              "3,4" : 0.6} # fill in table 1 here

    dist_2 = {"1,2" : 0.9, "1,3" : 0.4, "1,4" : 0.6, "1,5" : 0.9,
              "2,3" : 0.9, "2,4" : 0.9, "2,5" : 0.4,
              "3,4" : 0.6, "3,5" : 0.9,
              "4,5" : 0.9}

    # Check if dist_1 and dist_2 are ultrametric and additive by
    # calling is_ultrametric and is_additive with the default
    # threshold value (1e-4).
    #
    # YOUR CODE HERE
    #
    print("Dist 1")
    print("Ultrametric:", is_ultrametric(dist_1, 1e-4))
    print("Additive:", is_additive(dist_1, 1e-4))
    print()
    print("Dist 2")
    print("Ultrametric:", is_ultrametric(dist_2, 1e-4))
    print("Additive:", is_additive(dist_2, 1e-4))

    # Construct the ATPA synthase distance metric table
    atpa_table = {"1,2" : 0.5, "1,3" : 0.5, "1,4" : 0.1, "1,5" : 0.4, "1,6" : 0.4,
                  "2,3" : 0.3, "2,4" : 0.5, "2,5" : 0.5, "2,6" : 0.5,
                  "3,4" : 0.5, "3,5" : 0.5, "3,6" : 0.5,
                  "4,5" : 0.4, "4,6" : 0.4,
                  "5,6" : 0.3} #  fill in ATPA synthase distance metric table

    # Determine if the ATPA synthase distance metrics
    # are ultrametric and additive using the default
    # threshold value (1e-4).
    #
    # YOUR CODE HERE
    #    
    print()
    print("ATPA table")
    print("Ultrametric:", is_ultrametric(atpa_table, 1e-4))
    print("Additive:", is_additive(atpa_table, 1e-4))

# helper method for calculating the number of rows in dist
def rows(dist):
    x = len(dist)
    # solve n(1+n)=2x
    # n = (-1+sqrt(1+8x))/2
    # sqrt(1+8x) need to be cast to int, add 0.5 to prevent error with rounding and sqrt
    return int((int(sqrt(1+8*x) + 0.5) - 1)/2)


# helper method for retrieving entry dist
def fetch(x,y, dist):
    key = str(x) + "," + str(y)
    return dist[key]


# helper function to see if a group of three is ultrametric
def one_group_ultrametric(a, b, c, threshold=1e-4):
    order = [a, b, c]
    order.sort()
    return is_almost_equal(order[1], order[2], threshold)


def is_ultrametric(dist, threshold=1e-4):
    """Check that a set of pairs of point distances are ultrametric.

    Note: When making comparisons between distances, use `is_almost_equal` with
    the input parameterized threshold. This will be useful for subsequent
    problems where `is_ultrametric` is called. e.g. When comparing x and y, 
    also pass the threshold parameter: is_almost_equal(x, y, threshold).

    Args:
        dist (dict): exhaustive dict of pairs of points mapped to distances. 
        e.g.
            {"1,2" : 0.5, "1,3" : 0.1, "2,3" : 0.6}
        threshold (float): maximium difference in which numeric values are 
            considered equal
    Returns:
        (bool) True if the given distance metric is an ultrametric,
    False otherwise."""

    #
    # YOUR CODE HERE ()
    #
    n = rows(dist)
    for i in range(1,n):
        for j in range(i+1, n+1):
            for k in range(j+1, n+2):
                d_ij = fetch(i, j, dist)
                d_ik = fetch(i, k, dist)
                d_jk = fetch(j, k, dist)
                if not one_group_ultrametric(d_ij, d_ik, d_jk, threshold):
                    return False
    # when n = 1 skips cycle and returns true
    return True


def is_additive(dist, threshold=1e-4):
    """Check that a set of pairs of point distances are additive.

    Note: When making comparisons between distances, use `is_almost_equal` with
    the input parameterized threshold. This will be useful for subsequent
    problems where `is_ultrametric` is called. e.g. When comparing x and y, 
    also pass the threshold parameter: is_almost_equal(x, y, threshold).

    Args:
        dist (dict): exhaustive dict of pairs of points mapped to distances. 
        e.g.
            {"1,2" : 0.5, "1,3" : 0.1, "2,3" : 0.6}
        threshold (float): maximium difference in which numeric values are 
            considered equal

    Returns:
        (bool) Return True if the given distance metric is additive, 
        False otherwise."""

    #
    # YOUR CODE HERE ()
    #
    n = rows(dist)
    # when n = 2
    if n == 2:
        a = fetch(1, 2, dist)
        b = fetch(1, 3, dist)
        c = fetch(2, 3, dist)
        order = [a, b, c]
        order.sort()
        return (order[0] < order[2] - order[1]) | (is_almost_equal(order[0], order[2] - order[1], threshold))
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                for l in range(k + 1, n+2):
                    a = fetch(i, j, dist) + fetch(k, l, dist)
                    b = fetch(i, k, dist) + fetch(j, l, dist)
                    c = fetch(i, l, dist) + fetch(j, k, dist)
                    if not one_group_ultrametric(a, b, c, threshold):
                        return False
    # When n = 1 skips cycle and returns true
    return True


def is_almost_equal(num_1, num_2, threshold):
    """
    Return true if the difference between the two parameters is negligible
    enough that the parameters can be considered equal.
    """
    return abs(num_1 - num_2) <= threshold


if __name__ == '__main__':
    solve_ultrametric_additive()
