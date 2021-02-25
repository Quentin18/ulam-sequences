"""
Investigating Ulam sequences
Project Euler, Problem 167

Quentin Deschamps, 2021
"""
import time


def answer():
    """Return the answer to the problem."""
    start = time.time()
    result = 0
    # lengths of sequences to calculate to find period
    lengths = [200, 200, 1000, 5000, 20000, 200, 300000, 10**6, 10**7]
    for n, length in zip(range(2, 11), lengths):
        u = fast_ulam(2 * n + 1, 10**11, length)
        print(f'U(2, {2 * n + 1}) =', u)
        result += u
    # print results
    print('Result:', result)
    print('Runtime:', time.time() - start, 'seconds')


def fast_ulam(b, n, length=5000):
    """
    Return the n-th term of the Ulam sequence U(2, b).
    """
    # calculate sequences
    seq, diffs, pos_after_second_even = ulam2_diff(b, length)
    # period of the sequence of differences
    period = find_period(diffs, pos_after_second_even)
    print('Period:', period)
    # distance between the beginning of the period and the term to compute
    dist = n - pos_after_second_even - 1
    # calculate the term using the period
    return (dist // period) * (
        seq[pos_after_second_even + period] - seq[pos_after_second_even]
        ) + seq[pos_after_second_even + (dist % period)]


def ulam2_diff(b, n):
    """
    Return the n first terms of the Ulam sequence U(2, b),
    the sequence of differences between consecutive numbers,
    and the position after the second even term in the sequence.
    """
    seq = [2, b]                    # first two terms of the sequence
    s = {2, b}          # set of the terms of the sequence
    diffs = [seq[-1] - seq[-2]]     # sequence of differences
    length = 2                      # length of the sequence
    i = b + 1                       # number to test
    second_even = None  # second even term of the sequence (the first one is 2)
    pos_after_second_even = None    # position of the second even term
    while length < n:
        # count number of representations of i
        # as the sum of two previous members
        count = 0

        if second_even is None:
            # case second even not found
            for j in seq:
                if i - j in s and i - j > j:
                    count += 1

        else:
            # case second even found
            if i - 2 in s:
                count += 1
            if i - second_even in s:
                count += 1

        # i has unique representation, i is a ulam number
        if count == 1:
            diffs.append(i - seq[-1])
            seq.append(i)
            s.add(i)
            length += 1
            if second_even is None and i % 2 == 0:
                # second even found
                second_even = i
                pos_after_second_even = length
                i -= 1

        i += 1 if second_even is None else 2

    return seq, diffs, pos_after_second_even


def find_period(seq, start_pos):
    """
    Find the period of the sequence, beginning at start_pos.
    It returns None if no period found.
    """
    s = seq[start_pos:]
    length = len(s)
    for p in range(2, length // 2):
        for i in range(p, length):
            if s[i] != s[i % p]:
                break
        if i == length - 1:
            return p
    return None


if __name__ == '__main__':
    answer()
