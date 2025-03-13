#!/usr/bin/env python3
"""
total_term_count/mapper.py

Total term count refers to the total terms in each document.

Input: (docid+term, term_count)
Output: (docid, 1)
"""

import sys
import os

# Get document ID from the input file name
docid = os.path.splitext(os.path.basename(os.getenv('map_input_file', 'unknown.txt')))[0]

for line in sys.stdin.buffer.read().decode("utf-8", "replace").splitlines():
    print(line)
    for word in line.strip().split():
        # Keep only alphabetic characters and convert to lowercase
        term = ''.join(c for c in word.lower() if 'a' <= c <= 'z')
        if term: # Ensure term is not empty but do NOT filter out stop words in this step.
            print(f"{docid}\t1")
