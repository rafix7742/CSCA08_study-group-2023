""" CSCA08 Student-led study group (Dec 18th) time complexity solutions

For maximum learning, please try to solve the problems yourself before
looking at these solutions. These solutions are only one way to solve
the problems. There are many other ways to solve them. you may have
come up with a better solution yourself!

if there is any problem with the solutions, please let us know as soon as
possible, so we can fix it for everyone.
"""


# Question 1
def bad_partial_sum(lst: list[int]) -> list[int]:
    """ return a list with same length as ‘lst’ in which each
    Item in the output is the sum of respective item in ‘lst’
    And anything came before it

    >>> bad_partial_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> bad_partial_sum([1, 5, 2, 4, 5])
    [1, 6, 8, 12, 17]
    """
    # let n be the length of lst
    # because both of our loops are for-loops, the best case and worst case have
    # the same time complexity

    # One call
    result = []

    # Number of iterations: n
    for i in range(len(lst)):

        # Number of calls: once for each iteration of the outer loop
        result.append(lst[i])  # let this be command A

        # Number of iterations: i
        for j in range(i):
            # Number of calls: once for each iteration of the inner loop
            result[-1] = result[-1] + lst[j]  # let this be command B

        # number of command calls to B: i

    # number of command calls to A: n
    # number of command calls to B in total: 1 + 2 + 3 + ... + n = n(n+1)/2

    # total number of calls: n + n(n+1)/2 + 1 (for the first call)
    return result


def good_partial_sum(lst: list[int]) -> list[int]:
    """ return a list with same length as ‘lst’ in which each Item in the output
    is the sum of respective item in ‘lst’ and anything came before it

    >>> good_partial_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> good_partial_sum([1, 5, 2, 4, 5])
    [1, 6, 8, 12, 17]
    """
    # let n be the length of lst
    # because both of our loops are for-loops, the best case and worst case have
    # the same time complexity

    # One call
    result = [0] * len(lst)

    # One call
    result[0] = lst[0]

    # Number of iterations: n - 1
    for i in range(1, len(lst)):
        # Number of calls: once for each iteration of the outer loop
        result[i] = result[i - 1] + lst[i]  # let this be command A

    # number of command calls to A: n - 1

    # total number of calls: 1 + 1 + (n - 1) = n + 1
    return result


# Question 2
def power(n: int, k: int) -> int:
    """ return n^k

    >>> power(2, 3)
    8
    >>> power(5, 2)
    25
    """

    # one call
    result = 1

    # number of condition checks on each iteration: 1
    while k > 0:
        # number of calls: once for each iteration of the loop
        result = multiple(result, n)  # let this be command A

        # time complexity command A comes from multiple function which is 3k

        # number of assign statements: once for each iteration of the loop
        k = k - 1 # let this be command B

    # number of iterations: k

    # number of condition checks: k - 1
    # number of calls to A: k
    # number of calls to B: k

    # total number of calls: (k-1) + 3k * k + k + 1 (for the first call)
    #                     = 3k^2 + 2k
    return result


def multiple(n: int, k: int) -> int:
    """ return n*k

    >>> multiple(2, 3)
    6
    >>> multiple(5, 2)
    10
    """

    # one call
    result = 0

    # number of condition checks on each iteration: 1
    while k > 0:
        # number of calls: once for each iteration of the loop
        result = result + n # let this be command A

        # number of assign statements: once for each iteration of the loop
        k = k - 1 # let this be command B

    # number of iterations: k

    # number of condition checks: k - 1
    # number of calls to A: k
    # number of calls to B: k

    # total number of calls: 3k - 1 + 1 (for the first call) = 3k

    return result


# Question 3
def search(lst: list[int], target: int) -> int:
    """ return the index of the target in the list, if not found, return -1

    >>> search([1, 2, 3, 4], 3)
    2
    >>> search([1, 2, 3, 4], 5)
    -1
    """
    # let n be the length of lst

    # one call
    i = 0
    # one call
    j = len(lst) - 1

    # number of condition checks on each iteration: 1
    while i <= j:

        # number of condition checks: once for each iteration of the loop
        if lst[i] == target:
            return i

        # number of condition checks: once for each iteration of the loop
        if lst[j] == target:
            return j

        # number of assign statements: once for each iteration of the loop
        i = i + 1

        # number of assign statements: once for each iteration of the loop
        j = j - 1

    # best case: target is at the beginning or the end of the list
    # beginning: 1 + 1 + 1 = 3
    # end: 1 + 1 + 1 + 1 = 4

    # worst case: target is either no in the list or in the middle of the list
    # not in the list: 1 + 1 + n/2 + n/2 + n/2 = 3n/2 + 2
    # in the middle: 1 + 1 + 3 * (n/2 - 1) + 2 * (n/2) = 5n/2 - 1

    return -1


if __name__ == '__main__':
    print(bad_partial_sum([1, 2, 3, 4]))
    print(power(2, 3))
    print(search([1, 2, 3, 3, 4], 3))
