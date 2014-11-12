#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parse_input import parse
from dcg import dcg
from ndcg import ndcg
from pfound import pfound

def main():
    scores = parse()
    print('DCG: %f' % dcg(scores))
    print('NDCG: %f' % ndcg(scores))
    print('pFound: %f' % pfound(scores))    

if __name__ == "__main__":
    main()
