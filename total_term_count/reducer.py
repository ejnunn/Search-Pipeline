#!/usr/bin/env python3
"""
total_term_count/reducer.py

Total term count refers to the total terms in each document.
"""

import sys

current_word = None
current_count = 0
word = None

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from mapper.py
    parts = line.split('\t', 1)
    if len(parts) != 2:
        continue  # Skip malformed lines

    word, count = parts

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue  # Ignore/discard invalid lines

    # This works because Hadoop sorts map output by key (word) before passing to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word is not None:
            # Write result to STDOUT
            print(f"{current_word}\t{current_count}")
        current_count = count
        current_word = word

# Output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")
