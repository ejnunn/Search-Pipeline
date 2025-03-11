#!/usr/bin/env python3
"""
df/mapper.py


"""

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    docid_term, _ = line.split("\t")  # Extract docid+term
    docid, term = docid_term.split("+")

    # Emit (term, docid) once per occurrence in each document
    print(f"{term}\t{docid}")