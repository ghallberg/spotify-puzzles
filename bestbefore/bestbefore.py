#!/usr/bin/env python
"""Solution to the bestbefore problem presented at http://www.spotify.com/se/jobs/tech/best-before/"""
__author__ = "Gustaf Hallberg"
__copyrights__ = "Copyright 2013, Gustaf Hallberg"
__email__ = "ghallberg@gmail.com"

import sys
import datetime
import itertools


def first_possible_date(input):
    numbers = parse_numbers(input)
    candi_dates = itertools.permutations(numbers)
    actual_dates = tuple(filter(None,
                [actual_date(y, m, d) for y, m, d in candi_dates]
            ))

    return input + " is illegal" if not actual_dates else str(min(actual_dates))

def actual_date(year, month, day):
    try:
        return datetime.date(make_2k_year(year), month, day) 
    except:
        return None

def make_2k_year(num):
    if (num > 999 and (num > 2999 or num < 2000)) or num < 0:
        raise ValueError("Bad Year!")

    return num if num >= 2000 else num+2000

def parse_numbers(string):
    strings = string.split('/')
    return tuple([int(x) for x in strings])

if __name__ == '__main__':
    for line in sys.stdin:
        print(first_possible_date(line))


