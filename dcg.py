#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log2

def dcg(scores):
    summands = [(2 ** scores[i] - 1) / log2((i+1) + 1) for i in range(len(scores))]
    return sum(summands)
