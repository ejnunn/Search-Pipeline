#!/usr/bin/env python
"""
df/reducer.py


"""

import sys

current_term = None
current_docid = None
current_count = 0

# Input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    # Parse the mapper output: term \t docid
    term, docid = line.split('\t', 1)

    # Count unique docid entries for each term
    if term == current_term:
        if docid != current_docid:
            current_docid = docid
            current_count += 1
    else:
        # Output the previous term's DF count
        if current_term:
            print(f"{current_term}\t{current_count}")
        
        # Start counting for the new term
        current_term = term
        current_docid = docid
        current_count = 1

# Output the final term's DF count
if current_term:
    print(f"{current_term}\t{current_count}")
