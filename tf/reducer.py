#!/usr/bin/env python3
"""
tf/reducer.py

Term Frequency (TF) refers to the importance of each term to the document.
(i.e. the percentage of the document consists of each term)

Input: (docid, term, term_count)
Output: (docid, term, term_frequency)
"""

import sys

current_docid = None
total_terms = 0
term_counts = {}

# Read term counts from stdin
for line in sys.stdin:
    line = line.strip()
    docid, term, count = line.split("\t")

    try:
        count = int(count)
    except ValueError:
        continue  # Ignore invalid input

    if current_docid == docid:
        total_terms += count
        term_counts[term] = term_counts.get(term, 0) + count
    else:
        # Output TF for the previous document
        if current_docid:
            for term, term_count in term_counts.items():
                tf = term_count / total_terms
                print(f"{current_docid}+{term}\t{tf}")

        # Reset for new document
        current_docid = docid
        total_terms = count
        term_counts = {term: count}

# Output last document's TF values
if current_docid:
    for term, term_count in term_counts.items():
        tf = term_count / total_terms
        print(f"{current_docid}+{term}\t{tf}")
