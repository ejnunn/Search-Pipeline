#!/usr/bin/env python3
"""mapper.py"""

import sys
import os

# Extract document ID from filename
docid = os.path.splitext(os.path.basename(os.getenv('map_input_file', 'unknown')))[0]

for line in sys.stdin:
    for word in line.strip().split():
        lowered = word.lower()
        term = ''.join(filter(str.isalpha, lowered))  # Keep only alphabetic characters
        
        if term:
            print(f"{term}\t{docid}")
