#!/usr/bin/python
"""Solution to the reversebinary problem presented at http://www.spotify.com/se/jobs/tech/reversed-binary/"""
__author__ = "Gustaf Hallberg"
__copyrights__ = "Copyright 2013, Gustaf Hallberg"
__email__ = "ghallberg@gmail.com"

import sys

def reverse(input, previous = None):
    if previous == None:
        previous = []
    if input in (0,1):
        previous.append(input)
        previous.reverse()
        result = 0
        for i, bin_val in enumerate(previous):
            result = result + pow(2,i)*bin_val
        return result


    else:
        half, rest = divmod(input,2)
        previous.append(rest)
        return reverse(half, previous)

if __name__ == '__main__':
    for line in sys.stdin:
        print(reverse(int(line)))

