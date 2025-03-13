#!/usr/bin/env python3
"""
tf/mapper.py

Term Frequency (TF) refers to the importance of each term to the document.
(i.e. the percentage of the document consists of each term)

Input: (docid+term, term_count)
Output: (docid, term, term_count)
"""

import sys

for line in sys.stdin:
    words = line.strip().split()
    docid, term = words[0].split("+")
    count = words[1]
    print(f"{docid}\t{term}\t{count}")
