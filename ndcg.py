#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dcg import dcg

def idcg(scores):
    return dcg(sorted(scores, reverse = True))

def ndcg(scores):
    return dcg(scores) / idcg(scores)
    
