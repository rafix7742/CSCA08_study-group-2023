"""CSCA08 Student-led study group (Dec 18th) time complexity questions

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
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

    result = []
    for i in range(len(lst)):
        result.append(lst[i])
        for j in range(i):
            result[-1] = result[-1] + lst[j]
    return result


# Question 2
def power(n: int, k: int) -> int:
    """ return n^k

    >>> power(2, 3)
    8
    >>> power(5, 2)
    25
    """
    result = 1
    while k > 0:
        result = multiple(result, n)

        k = k - 1

    return result


def multiple(n: int, k: int) -> int:
    """ return n*k

    >>> multiple(2, 3)
    6
    >>> multiple(5, 2)
    10
    """

    result = 0
    while k > 0:
        result = result + n

        k = k - 1

    return result


# Question 3
def search(lst: list[int], target: int) -> int:
    """ return the index of the target in the list, if not found, return -1

    >>> search([1, 2, 3, 4], 3)
    2
    >>> search([1, 2, 3, 4], 5)
    -1
    """

    i = 0
    j = len(lst) - 1
    while i <= j:
        if lst[i] == target:
            return i
        if lst[j] == target:
            return j
        i = i + 1
        j = j - 1

    return -1


if __name__ == '__main__':
    print(bad_partial_sum([1, 2, 3, 4]))
    print(power(2, 3))
    print(search([1, 2, 3, 3, 4], 3))
