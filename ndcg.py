#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dcg import dcg

def idcg(scores):
    return dcg(sorted(scores, reverse = True))

def ndcg(scores):
    return dcg(scores) / idcg(scores)

def simple_test():
    scores = [2, 3, 1, 0, 0, 2, 0, 2, 0, 1]
    print(ndcg(scores))

if __name__ == "__main__":
    simple_test()
    
