#!/usr/bin/env python3
"""term_count/mapper.py"""

import sys
import os

# Add the 'utils' directory to the sys.path to be able to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

# Now import the stop_words set from utils.py
from utils import stop_words

def get_docid():
    """Extract document ID from Hadoop's environment or fallback for local use."""
    filepath = os.getenv('map_input_file')
    if filepath:
        return os.path.splitext(os.path.basename(filepath))[0]
    return "unknown_doc"  # Fallback when running locally without Hadoop

docid = get_docid()

for line in sys.stdin.buffer.read().decode("utf-8", "replace"):
    for word in line.strip().split():
        lowered = word.lower()
        term = "".join(filter(lambda c: 97 <= ord(c) <= 122, lowered)) # Only lowercase a-z

        if term and term not in stop_words:  # Filter out stop words
            print(f"{docid}+{term}\t1")
