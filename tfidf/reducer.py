#!/usr/bin/env python3
"""
tfidf/reducer.py

Input: word ((word, docid), (wordcount, wordperdoc))
Output: ((word, docid), tf_idf)
"""

import sys
from math import log

N = int(sys.argv[1])  # Number of files in the corpus

current_term = None
df_value = 0
tf_entries = []  # Store TF entries until DF value is known

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    term, tag, value = line.split("\t") # e.g. (word, TF, 2)

    # New term — process the previous term's data
    if term != current_term:
        # Compute TF-IDF for the previous term
        for tf_entry in tf_entries:
            docid, tf = tf_entry.split("+")
            tfidf = float(tf) * log(N / df_value)
            print(f"{docid}+{current_term}\t{tfidf}")
        
        # Reset state for the new term
        current_term = term
        df_value = 0
        tf_entries = []

    # Store DF or TF data
    if tag == "DF":
        df_value = int(value)
    elif tag == "TF":
        tf_entries.append(value)

# Final term's data
if current_term:
    for tf_entry in tf_entries:
        docid, tf = tf_entry.split("+")
        tfidf = float(tf) * log(N / df_value)
        print(f"{docid}+{current_term}\t{tfidf}")
