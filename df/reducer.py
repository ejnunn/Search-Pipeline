#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_docid = None
current_count = 0
current_term = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    term, docid = line.split('\t', 1)
    
    # only count a unique docid
    if term == current_term:
        if docid != current_docid:
            current_docid = docid
            current_count += 1
    # once new term is read, print out previous term's unique docid count
    else:
        if current_term:
            print '%s\t%s' % (current_term, current_count)
        current_term = term
        current_docid = docid
        current_count = 1
        
    
# do not forget to output the last term if needed!
if term == current_term:
    print '%s\t%s' % (current_term, current_count)
