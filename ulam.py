"""
Ulam sequences

Quentin Deschamps, 2021
"""
import time


def ulam(a, b, n):
    """
    Return the n-th term of the Ulam sequence U(a, b).
    """
    seq = [a, b]    # first two terms of the sequence
    length = 2      # length of the sequence
    i = b + 1       # number to test
    while length < n:
        # count number of representations of i
        # as the sum of two previous members
        count = 0
        for j in range(length - 1):
            for k in range(j + 1, length):
                if seq[j] + seq[k] == i:
                    count += 1
                if count > 1:   # two representations
                    break
            if count > 1:   # two representations
                break

        # i has unique representation, i is a ulam number
        if count == 1:
            seq.append(i)
            length += 1

        i += 1

    return seq[n - 1]


def ulam2(b, n):
    """
    Return the n-th term of the Ulam sequence U(2, b).
    """
    seq = [2, b]        # first two terms of the sequence
    length = 2          # length of the sequence
    i = b + 1           # number to test
    second_even = None  # second even term of the sequence (the first one is 2)
    while length < n:
        # count number of representations of i
        # as the sum of two previous members
        count = 0

        if second_even is None:
            # case second even not found
            for j in range(length - 1):
                for k in range(j + 1, length):
                    if seq[j] + seq[k] == i:
                        count += 1
                    if count > 1:   # two representations
                        break
                if count > 1:   # two representations
                    break

        else:
            # case second even found
            if i - 2 in seq:
                count += 1
            if i - second_even in seq:
                count += 1

        # i has unique representation, i is a ulam number
        if count == 1:
            seq.append(i)
            length += 1
            if second_even is None and i % 2 == 0:
                # second even found
                second_even = i
                i -= 1

        i += 1 if second_even is None else 2

    return seq[n - 1]


if __name__ == '__main__':
    start = time.time()
    print(ulam(2, 5, 1000))
    print(f'Found in {time.time() - start} seconds')

    start = time.time()
    print(ulam2(5, 1000))
    print(f'Found in {time.time() - start} seconds')
