#!/usr/bin/python

import sys
import heapq
from collections import Counter

words = []

# read words from input file into words list
with open(sys.argv[1]) as f:
    for line in f:
        for word in line.split():
            words.append(word)
    
# build dictionary with frequency counts of all words
word_freq = Counter(words)
    
# build heap of top 10 frequent elements, convert to output array
result = heapq.nlargest(10, word_freq, key=word_freq.get)

# print list of top 10 frequent words
print(result)
            
    
            
    