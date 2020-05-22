#!/usr/bin/env python
"""mapper.py"""

import sys
import string
import os


for line in sys.stdin:
    words = line.strip().split()
    docid, term = words[0].split("+")
    count = words[1]
    print '%s\t%s\t%s' % (docid, term, count)
