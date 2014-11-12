#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_plook(scores, pbreak):
    res = [1 - pbreak]
    for i in range(1, len(scores)):
        res.append(res[i-1] * (1 - scores[i-1]) * (1 - pbreak))
    return res

def calc_prel(scores):
    max_score = max(scores)
    return [(2 ** scores[i] - 1) / (2 ** max_score) for i in range(len(scores))]

def pfound(scores, pbreak = 0.15):
    prel = calc_prel(scores)
    plook = calc_plook(prel, pbreak)
    summands = [plook[i] * prel[i] for i in range(len(prel))] 
    return sum(summands)
