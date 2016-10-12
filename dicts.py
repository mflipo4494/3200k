
def hist(s):
    """returns the histogram of the characters in s

    >>> hist("AAGGT")
    {'A': 2, 'T': 1, 'G': 2}

    >>> hist("!!xx")
    {'!': 2, 'x': 2}

    """
    results = {}
    for x in s:
        results[x] = s.count(x)
    return results


def str_to_int(s):
    """converts a string to an integer value

    >>> str_to_int('s')
    115

    >>> str_to_int('st!ll')
    11511633108108L

    hint: the built in ord and chr functions

    """
    results = []
    for x in s:
        results.append(str(ord(x)))
    return int("".join(results))


def null_list(length):
    """return a list of all None values of given length

    >>> null_list(3)
    [None, None, None]

    >>> null_list(1)
    [None]

    """
    results = range(length)
    for x in results:
        results[x] = None
    return results
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
