"""
module for sixth lab algo
"""


def create_pi_list(needle):
    """
    Function to create list with prefixes
    :param needle: needle string
    :return: list with prefixes
    """
    n = len(needle)
    pi_list = [0] * n
    j = 0
    i = 1

    while i < n:
        if needle[i] == needle[j]:
            pi_list[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                pi_list[i] = 0
                i += 1
            else:
                j = pi_list[j - 1]

    return pi_list


def kmp(haystack, needle):
    """
    Function to find all start indexes needle string in haystack string
    :param haystack:
    :param needle:
    :return: list with all start indexes
    """
    if not haystack or not needle:
        return []

    indexes = []
    pi_list = create_pi_list(needle)
    m = len(needle)

    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                indexes.append(i - j)
                j = pi_list[j - 1]
        else:
            if j > 0:
                j = pi_list[j - 1]
            else:
                i += 1

    return indexes
