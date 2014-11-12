#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log2

def dcg(scores):
    summands = [(2 ** scores[i] - 1) / log2((i+1) + 1) for i in range(len(scores))]
    return sum(summands)

def simple_test():
    scores = [2, 3, 1, 0, 0, 2, 0, 2, 0, 1]
    print(dcg(scores))

if __name__ == "__main__":
    simple_test()
