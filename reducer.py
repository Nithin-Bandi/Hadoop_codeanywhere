#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

# Read each line from standard input
for line in sys.stdin:
    # Split the line into word and count
    word, count = line.strip().split("\t", 1)
    try:
        count = int(count)
    except ValueError:
        continue  # Skip lines where count is not a number

    # If the word is the same as the previous one, increment its count
    if word == current_word:
        current_count += count
    else:
        # If it's a new word and not the first line, print the word and its total count
        if current_word:
            print(f"{current_word}\t{current_count}")
        
        # Reset counters for the new word
        current_word = word
        current_count = count

# Output the final word and its count
if current_word == word:
    print(f"{current_word}\t{current_count}")
