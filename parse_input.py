#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit

def parse():
    if len(argv) != 2:
        print('incorrect input. filename required.')
        exit(1)
    filename = argv[1]
    f = open(filename, 'r')
    n = int(f.readline())
    scores = [int(x) for x in f.readline().split()]
    if len(scores) != n:
        print('incorrect file format')
        exit(1)
    return scores
    
