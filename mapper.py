#!/usr/bin/env python

import sys

# Read each line from standard input
for line in sys.stdin:
    # Split the line into words
    words = line.strip().split()
    
    # Output each word with a count of 1
    for word in words:
        print(f"{word}\t1")
