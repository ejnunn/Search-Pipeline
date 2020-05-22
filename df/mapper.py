#!/usr/bin/env python
"""mapper.py"""

import sys
import string
import os

docid = os.path.splitext(os.path.basename(os.getenv('map_input_file')))[0]

for line in sys.stdin:
    for word in line.strip().split():
        lowered = word.lower()
        term  = filter(lambda c: 97 <= ord(c) <= 122, lowered)
        if len(term) > 0:
            print '%s\t%s' % (term, docid)
